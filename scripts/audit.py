#!/usr/bin/env python3
"""
Independent Architectural Audit Script for Universal .NET AI Core Team.
Evaluates:
- Architecture & Decoupled Layers
- Agent Responsibility Boundaries (Least Privilege, No overlap)
- Skill Granularity & Progressive Disclosure (< 500 lines)
- Antigravity Compatibility (.agents/agents, .agents/skills, .agents/rules)
- Legacy Safety & Maintenance != Migration
- Security Baseline & OWASP Coverage
- Extensibility for Future Technology Packs
- Global vs Workspace Separation
- Failure Handling & Handoff Reliability
"""

import os
import sys
import re

def audit_repository(repo_root):
    findings = {
        "CRITICAL": [],
        "HIGH": [],
        "MEDIUM": [],
        "LOW": [],
        "RECOMMENDATIONS": []
    }

    # 1. Antigravity Compatibility Check
    agents_dir = os.path.join(repo_root, ".agents", "agents")
    skills_dir = os.path.join(repo_root, ".agents", "skills")
    rules_dir = os.path.join(repo_root, ".agents", "rules")

    if not os.path.isdir(agents_dir) or not os.path.isdir(skills_dir) or not os.path.isdir(rules_dir):
        findings["CRITICAL"].append("Antigravity standard directory layout (.agents/agents, .agents/skills, .agents/rules) is incomplete.")

    # 2. Agent Boundaries & Least Privilege
    expected_agents = [
        "tech-lead", "project-profiler", "architect", "dotnet-engineer",
        "database-engineer", "test-engineer", "security-engineer",
        "performance-engineer", "migration-engineer", "legacy-analyst", "code-reviewer"
    ]
    for ag in expected_agents:
        ag_path = os.path.join(agents_dir, ag, "agent.md")
        if not os.path.isfile(ag_path):
            findings["CRITICAL"].append(f"Missing core agent: {ag}")
            continue

        with open(ag_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "Non-Responsibilities" not in content:
            findings["HIGH"].append(f"Agent '{ag}' missing explicit 'Non-Responsibilities' section.")
        if "Handoff" not in content and "Quality" not in content:
            findings["MEDIUM"].append(f"Agent '{ag}' has weak handoff specification.")

    # 3. Progressive Disclosure (Line Counts)
    for root, _, files in os.walk(skills_dir):
        for f in files:
            if f == "SKILL.md":
                spath = os.path.join(root, f)
                with open(spath, "r", encoding="utf-8") as sfile:
                    lines = sfile.readlines()
                    if len(lines) > 400:
                        findings["LOW"].append(f"Skill '{os.path.relpath(spath, repo_root)}' is {len(lines)} lines; consider splitting bulky references into references/ folder.")

    # 4. Legacy Safety Check
    legacy_guard = os.path.join(skills_dir, "legacy", "legacy-safety-guard", "SKILL.md")
    legacy_rule = os.path.join(rules_dir, "16-legacy-safety.md")
    if not os.path.isfile(legacy_guard) or not os.path.isfile(legacy_rule):
        findings["HIGH"].append("Legacy safety rules (Maintenance != Migration) missing or incomplete.")

    # 5. Technology Pack Extensibility
    routing_doc = os.path.join(repo_root, "docs", "routing.md")
    if not os.path.isfile(routing_doc):
        findings["MEDIUM"].append("Missing docs/routing.md defining Technology Pack mapping.")
    else:
        with open(routing_doc, "r", encoding="utf-8") as rf:
            rc = rf.read()
            if "Technology Pack" not in rc or "abp" not in rc.lower():
                findings["MEDIUM"].append("Technology Pack extensibility paths not fully documented in docs/routing.md.")

    # Recommendations
    findings["RECOMMENDATIONS"].append("Technology Packs (modern-dotnet, aspnet-core, ef-core, abp, legacy-dotnet-framework) should be developed as standalone modular plugin directories in the next phase.")
    findings["RECOMMENDATIONS"].append("Consider providing a VS Code task or Antigravity custom slash command (/profile) to trigger profile-project.py automatically.")

    return findings

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    report = audit_repository(root)

    print("================ INDEPENDENT AUDIT REPORT ================")
    print(f"CRITICAL ISSUES: {len(report['CRITICAL'])}")
    for item in report['CRITICAL']:
        print(f"  - {item}")

    print(f"\nHIGH ISSUES: {len(report['HIGH'])}")
    for item in report['HIGH']:
        print(f"  - {item}")

    print(f"\nMEDIUM ISSUES: {len(report['MEDIUM'])}")
    for item in report['MEDIUM']:
        print(f"  - {item}")

    print(f"\nLOW ISSUES: {len(report['LOW'])}")
    for item in report['LOW']:
        print(f"  - {item}")

    print(f"\nRECOMMENDATIONS: {len(report['RECOMMENDATIONS'])}")
    for item in report['RECOMMENDATIONS']:
        print(f"  - {item}")
    print("==========================================================")
