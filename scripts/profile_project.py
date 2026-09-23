#!/usr/bin/env python3
"""
Authoritative Project Profiler Engine for .NET Solutions.
Inspects solution files, csproj metadata, packages.config, web.config, and global.json
to generate .project-context.json and .project-context.md without modifying any files.
"""

import os
import sys
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

def parse_xml_safely(file_path):
    try:
        tree = ET.parse(file_path)
        return tree.getroot()
    except Exception:
        return None

def profile_directory(target_dir):
    profile = {
        "project_name": os.path.basename(os.path.abspath(target_dir)),
        "analyzed_at": datetime.now(timezone.utc).isoformat(),
        "solution_files": [],
        "runtime": {
            "generation": "unknown",
            "target_frameworks": [],
            "csharp_version": "unknown",
            "nullable_enabled": False,
            "global_json_sdk": None
        },
        "web": {
            "framework": "none",
            "style": "none"
        },
        "data_access": {
            "orm": "none",
            "database": "none",
            "migrations": "none"
        },
        "enterprise": {
            "abp_framework": False,
            "abp_version": None
        },
        "testing": {
            "frameworks": [],
            "mocking": [],
            "assertions": []
        },
        "architecture_pattern": "n-tier",
        "legacy_indicators": {
            "has_packages_config": False,
            "has_web_config": False,
            "has_wcf": False,
            "has_sync_context_dependency": False
        },
        "resolved_skills": []
    }

    # 1. Inspect global.json
    global_json_path = os.path.join(target_dir, "global.json")
    if os.path.isfile(global_json_path):
        try:
            with open(global_json_path, "r", encoding="utf-8") as f:
                gj = json.load(f)
                sdk_ver = gj.get("sdk", {}).get("version")
                profile["runtime"]["global_json_sdk"] = sdk_ver
        except Exception:
            pass

    # 2. Discover solutions and metadata files
    all_files = []
    for root, _, files in os.walk(target_dir):
        for f in files:
            all_files.append(os.path.join(root, f))

    for fpath in all_files:
        fname = os.path.basename(fpath).lower()
        if fname.endswith(".sln") or fname.endswith(".slnx"):
            profile["solution_files"].append(os.path.relpath(fpath, target_dir).replace("\\", "/"))
        elif fname == "packages.config":
            profile["legacy_indicators"]["has_packages_config"] = True
        elif fname == "web.config":
            profile["legacy_indicators"]["has_web_config"] = True

    # 3. Inspect .csproj files
    csproj_files = [f for f in all_files if f.lower().endswith(".csproj")]
    detected_frameworks = set()
    has_legacy_fx = False
    has_modern_dotnet = False

    for csproj in csproj_files:
        try:
            with open(csproj, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception:
            continue

        # TargetFramework(s)
        tf_match = re.findall(r"<TargetFramework>(.*?)</TargetFramework>", content, re.IGNORECASE)
        tfs_match = re.findall(r"<TargetFrameworks>(.*?)</TargetFrameworks>", content, re.IGNORECASE)
        tf_version = re.findall(r"<TargetFrameworkVersion>(.*?)</TargetFrameworkVersion>", content, re.IGNORECASE)

        for tf in tf_match:
            detected_frameworks.add(tf.strip())
        for tfs in tfs_match:
            for part in tfs.split(";"):
                if part.strip():
                    detected_frameworks.add(part.strip())
        for tfv in tf_version:
            detected_frameworks.add(tfv.strip())

        # Nullable
        if "<Nullable>enable</Nullable>" in content or "<Nullable>warnings</Nullable>" in content:
            profile["runtime"]["nullable_enabled"] = True

        # LangVersion
        lang_match = re.search(r"<LangVersion>(.*?)</LangVersion>", content, re.IGNORECASE)
        if lang_match:
            profile["runtime"]["csharp_version"] = lang_match.group(1).strip()

        # Web indicators
        if "Microsoft.AspNetCore" in content or 'Sdk="Microsoft.NET.Sdk.Web"' in content:
            profile["web"]["framework"] = "aspnet-core"
            if "minimal" in content.lower() or "mapget" in content.lower():
                profile["web"]["style"] = "minimal-apis"
            else:
                profile["web"]["style"] = "controllers"
        elif "System.Web.Mvc" in content or "Microsoft.AspNet.Mvc" in content:
            profile["web"]["framework"] = "mvc5"
            profile["web"]["style"] = "controllers"
        elif "System.Web.Http" in content or "Microsoft.AspNet.WebApi" in content:
            if profile["web"]["framework"] == "none":
                profile["web"]["framework"] = "webapi2"
                profile["web"]["style"] = "controllers"
        elif "System.ServiceModel" in content or ".svc" in content:
            profile["legacy_indicators"]["has_wcf"] = True
            if profile["web"]["framework"] == "none":
                profile["web"]["framework"] = "wcf"
                profile["web"]["style"] = "wcf-services"

        # Data Access / ORM
        if "Microsoft.EntityFrameworkCore" in content:
            profile["data_access"]["orm"] = "ef-core"
            profile["data_access"]["migrations"] = "ef-core-migrations"
            if "Npgsql" in content:
                profile["data_access"]["database"] = "postgresql"
            elif "SqlServer" in content:
                profile["data_access"]["database"] = "sql-server"
            elif "Sqlite" in content:
                profile["data_access"]["database"] = "sqlite"
        elif "EntityFramework" in content and "Microsoft.EntityFrameworkCore" not in content:
            profile["data_access"]["orm"] = "ef6"
            profile["data_access"]["migrations"] = "ef6-code-first"
            profile["data_access"]["database"] = "sql-server"
        elif "Dapper" in content:
            profile["data_access"]["orm"] = "dapper"
            profile["data_access"]["database"] = "sql-server"

        # Enterprise: ABP Framework
        if "Volo.Abp" in content:
            profile["enterprise"]["abp_framework"] = True
            abp_m = re.search(r'Include="Volo\.Abp\.[^"]*"\s+Version="([^"]+)"', content)
            if abp_m:
                profile["enterprise"]["abp_version"] = abp_m.group(1)

        # Testing
        if "xunit" in content.lower():
            if "xunit" not in profile["testing"]["frameworks"]:
                profile["testing"]["frameworks"].append("xunit")
        if "nunit" in content.lower():
            if "nunit" not in profile["testing"]["frameworks"]:
                profile["testing"]["frameworks"].append("nunit")
        if "mstest" in content.lower() or "microsoft.visualstudio.testplatform" in content.lower():
            if "mstest" not in profile["testing"]["frameworks"]:
                profile["testing"]["frameworks"].append("mstest")
        if "fluentassertions" in content.lower():
            profile["testing"]["assertions"].append("fluentassertions")
        if "moq" in content.lower():
            profile["testing"]["mocking"].append("moq")
        if "nsubstitute" in content.lower():
            profile["testing"]["mocking"].append("nsubstitute")

    # Also inspect web.config if present
    for fpath in all_files:
        if os.path.basename(fpath).lower() == "web.config":
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    wc = f.read()
                    if "System.Web.Mvc" in wc and profile["web"]["framework"] == "none":
                        profile["web"]["framework"] = "mvc5"
                        profile["web"]["style"] = "controllers"
                    if "EntityFramework" in wc and profile["data_access"]["orm"] == "none":
                        profile["data_access"]["orm"] = "ef6"
                        profile["data_access"]["database"] = "sql-server"
                    if "system.serviceModel" in wc:
                        profile["legacy_indicators"]["has_wcf"] = True
            except Exception:
                pass

    # 4. Synthesize runtime generation
    profile["runtime"]["target_frameworks"] = sorted(list(detected_frameworks))
    for tf in profile["runtime"]["target_frameworks"]:
        tf_l = tf.lower()
        if "v4." in tf_l or "net4" in tf_l or "v3." in tf_l or "v2." in tf_l:
            has_legacy_fx = True
        elif "net8" in tf_l or "net9" in tf_l or "net10" in tf_l:
            has_modern_dotnet = True
        elif "netcoreapp" in tf_l or "net6" in tf_l or "net7" in tf_l or "net5" in tf_l:
            has_modern_dotnet = True

    if not detected_frameworks and not profile["solution_files"]:
        profile["runtime"]["generation"] = "unknown"
        profile["architecture_pattern"] = "unknown"
        profile["resolved_skills"] = []
        return profile

    if has_legacy_fx and has_modern_dotnet:
        profile["runtime"]["generation"] = "mixed"
    elif has_legacy_fx:
        profile["runtime"]["generation"] = "legacy-framework"
        if profile["runtime"]["csharp_version"] == "unknown":
            profile["runtime"]["csharp_version"] = "7.3"
    elif has_modern_dotnet:
        profile["runtime"]["generation"] = "modern-dotnet"
        if profile["runtime"]["csharp_version"] == "unknown":
            profile["runtime"]["csharp_version"] = "12.0"
    else:
        profile["runtime"]["generation"] = "modern-dotnet"
        if profile["runtime"]["csharp_version"] == "unknown":
            profile["runtime"]["csharp_version"] = "12.0"

    # 5. Architecture pattern heuristic
    if profile["enterprise"]["abp_framework"]:
        profile["architecture_pattern"] = "modular-monolith"
    elif any("clean" in f.lower() or "domain" in f.lower() for f in all_files):
        profile["architecture_pattern"] = "clean-architecture"
    elif any("features" in f.lower() or "endpoints" in f.lower() for f in all_files):
        profile["architecture_pattern"] = "vertical-slice"
    elif profile["legacy_indicators"]["has_web_config"]:
        profile["architecture_pattern"] = "classic-mvc"
    else:
        profile["architecture_pattern"] = "n-tier"

    # 6. Resolve Skills
    resolved = ["skills/engineering/evidence-first", "skills/engineering/minimal-change"]

    if profile["runtime"]["generation"] in ["legacy-framework", "mixed"] or profile["legacy_indicators"]["has_web_config"]:
        resolved.append("skills/legacy/legacy-safety-guard")
        resolved.append("skills/project-analysis/legacy-discovery")

    resolved.append("skills/coding/csharp-idioms")

    if profile["data_access"]["orm"] in ["ef-core", "ef6"]:
        resolved.append("skills/database/ef-diagnostics")
    if profile["data_access"]["orm"] in ["dapper", "ado-net"] or profile["data_access"]["database"] != "none":
        resolved.append("skills/database/sql-safety")

    if profile["web"]["framework"] in ["aspnet-core", "mvc5", "webapi2"]:
        resolved.append("skills/security/secure-by-default")
        resolved.append("skills/security/secrets-audit")
        resolved.append("skills/coding/error-handling-result")

    if profile["testing"]["frameworks"]:
        resolved.append("skills/testing/test-pyramid")
        resolved.append("skills/testing/regression-testing")

    if profile["architecture_pattern"] in ["clean-architecture", "modular-monolith"]:
        resolved.append("skills/architecture/clean-boundaries")
        resolved.append("skills/architecture/adr-management")

    profile["resolved_skills"] = sorted(list(set(resolved)))

    return profile

def write_profile_artifacts(profile, output_dir):
    json_path = os.path.join(output_dir, ".project-context.json")
    md_path = os.path.join(output_dir, ".project-context.md")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)

    md_content = f"""# Project Context: {profile['project_name']}

Generated at: `{profile['analyzed_at']}`
Authoritative Profile: [`.project-context.json`](file:///.project-context.json)

---

## 1. Runtime & Language Environment
- **Generation**: `{profile['runtime']['generation']}`
- **Target Framework(s)**: `{", ".join(profile['runtime']['target_frameworks']) or "Unknown"}`
- **Effective C# Version**: `{profile['runtime']['csharp_version']}`
- **Nullable Context**: `{"Enabled" if profile['runtime']['nullable_enabled'] else "Disabled"}`
- **SDK Version**: `{profile['runtime']['global_json_sdk'] or "Default"}`

## 2. Web & API Framework
- **Web Stack**: `{profile['web']['framework']}`
- **Routing & Endpoints**: `{profile['web']['style']}`

## 3. Data Persistence & Modeling
- **ORM / Data Access**: `{profile['data_access']['orm']}`
- **Underlying Database**: `{profile['data_access']['database']}`
- **Migration Strategy**: `{profile['data_access']['migrations']}`

## 4. Enterprise & Third-Party Frameworks
- **ABP Framework**: `{"Yes (v" + str(profile['enterprise']['abp_version']) + ")" if profile['enterprise']['abp_framework'] else "No"}`

## 5. Testing Infrastructure
- **Test Runner(s)**: `{", ".join(profile['testing']['frameworks']) or "None detected"}`
- **Mocking Library**: `{", ".join(profile['testing']['mocking']) or "None"}`
- **Assertions**: `{", ".join(profile['testing']['assertions']) or "Standard"}`

## 6. Architectural Topology
- **Pattern**: `{profile['architecture_pattern']}`
- **Legacy Indicators**:
  - `packages.config`: `{profile['legacy_indicators']['has_packages_config']}`
  - `web.config`: `{profile['legacy_indicators']['has_web_config']}`
  - `WCF / ASMX`: `{profile['legacy_indicators']['has_wcf']}`

## 7. Resolved Skills & Active Technology Packs
The following skills have been automatically activated for this solution:
"""
    for sk in profile["resolved_skills"]:
        md_content += f"- `{sk}`\n"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    return json_path, md_path

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    out_dir = sys.argv[2] if len(sys.argv) > 2 else target
    prof = profile_directory(target)
    j_p, m_p = write_profile_artifacts(prof, out_dir)
    print(f"Successfully profiled project in '{target}'.")
    print(f"Generated: {j_p} and {m_p}")
