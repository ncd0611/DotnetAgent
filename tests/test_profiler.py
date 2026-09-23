#!/usr/bin/env python3
"""
Test Suite for Project Profiler against the 6 Representative Test Fixtures using standard unittest.
"""

import os
import sys
import unittest

# Add scripts directory to sys.path
scripts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts")
sys.path.insert(0, scripts_dir)

from profile_project import profile_directory

FIXTURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")

class TestProjectProfiler(unittest.TestCase):

    def test_fixture_1_legacy_mvc5(self):
        target = os.path.join(FIXTURES_DIR, "fixture-1-legacy-mvc5")
        profile = profile_directory(target)

        self.assertEqual(profile["runtime"]["generation"], "legacy-framework")
        self.assertIn("v4.8", profile["runtime"]["target_frameworks"])
        self.assertEqual(profile["runtime"]["csharp_version"], "7.3")
        self.assertEqual(profile["web"]["framework"], "mvc5")
        self.assertEqual(profile["data_access"]["orm"], "ef6")
        self.assertTrue(profile["legacy_indicators"]["has_packages_config"])
        self.assertTrue(profile["legacy_indicators"]["has_web_config"])
        self.assertIn("skills/legacy/legacy-safety-guard", profile["resolved_skills"])
        self.assertIn("skills/database/ef-diagnostics", profile["resolved_skills"])

    def test_fixture_2_net8_aspnet_core(self):
        target = os.path.join(FIXTURES_DIR, "fixture-2-net8-aspnet-core")
        profile = profile_directory(target)

        self.assertEqual(profile["runtime"]["generation"], "modern-dotnet")
        self.assertIn("net8.0", profile["runtime"]["target_frameworks"])
        self.assertTrue(profile["runtime"]["nullable_enabled"])
        self.assertEqual(profile["web"]["framework"], "aspnet-core")
        self.assertEqual(profile["data_access"]["orm"], "ef-core")
        self.assertEqual(profile["data_access"]["database"], "postgresql")
        self.assertIn("xunit", profile["testing"]["frameworks"])
        self.assertIn("skills/coding/csharp-idioms", profile["resolved_skills"])
        self.assertIn("skills/database/ef-diagnostics", profile["resolved_skills"])
        self.assertIn("skills/testing/test-pyramid", profile["resolved_skills"])

    def test_fixture_3_net10_modern(self):
        target = os.path.join(FIXTURES_DIR, "fixture-3-net10-modern")
        profile = profile_directory(target)

        self.assertEqual(profile["runtime"]["generation"], "modern-dotnet")
        self.assertIn("net10.0", profile["runtime"]["target_frameworks"])
        self.assertEqual(profile["runtime"]["csharp_version"], "13.0")
        self.assertEqual(profile["runtime"]["global_json_sdk"], "10.0.100")
        self.assertEqual(profile["data_access"]["orm"], "ef-core")
        self.assertEqual(profile["data_access"]["database"], "sqlite")

    def test_fixture_4_abp_efcore(self):
        target = os.path.join(FIXTURES_DIR, "fixture-4-abp-efcore")
        profile = profile_directory(target)

        self.assertTrue(profile["enterprise"]["abp_framework"])
        self.assertEqual(profile["enterprise"]["abp_version"], "9.0.2")
        self.assertEqual(profile["architecture_pattern"], "modular-monolith")
        self.assertEqual(profile["data_access"]["orm"], "ef-core")
        self.assertEqual(profile["data_access"]["database"], "sql-server")
        self.assertIn("skills/architecture/clean-boundaries", profile["resolved_skills"])

    def test_fixture_5_dapper_api(self):
        target = os.path.join(FIXTURES_DIR, "fixture-5-dapper-api")
        profile = profile_directory(target)

        self.assertEqual(profile["runtime"]["generation"], "modern-dotnet")
        self.assertEqual(profile["data_access"]["orm"], "dapper")
        self.assertEqual(profile["data_access"]["database"], "sql-server")
        self.assertIn("skills/database/sql-safety", profile["resolved_skills"])

    def test_fixture_6_mixed_legacy_sln(self):
        target = os.path.join(FIXTURES_DIR, "fixture-6-mixed-legacy-sln")
        profile = profile_directory(target)

        self.assertEqual(profile["runtime"]["generation"], "mixed")
        self.assertTrue(profile["legacy_indicators"]["has_wcf"])
        self.assertIn("v4.7.2", profile["runtime"]["target_frameworks"])
        self.assertIn("net8.0", profile["runtime"]["target_frameworks"])
        self.assertIn("netstandard2.0", profile["runtime"]["target_frameworks"])
        self.assertIn("skills/legacy/legacy-safety-guard", profile["resolved_skills"])

    def test_empty_or_non_dotnet_directory(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            profile = profile_directory(tmpdir)
            self.assertEqual(profile["runtime"]["generation"], "unknown")
            self.assertEqual(profile["runtime"]["csharp_version"], "unknown")
            self.assertEqual(profile["architecture_pattern"], "unknown")
            self.assertEqual(profile["resolved_skills"], [])

if __name__ == "__main__":
    unittest.main()
