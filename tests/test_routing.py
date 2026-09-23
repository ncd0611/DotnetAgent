#!/usr/bin/env python3
"""
Test Suite for Task Routing Scenarios (Scenarios A through H) using standard unittest.
"""

import unittest

SCENARIOS = {
    "A": {
        "title": "Add CRUD endpoint",
        "stack": {"generation": "modern-dotnet", "framework": "aspnet-core"},
        "expected_agents": ["dotnet-engineer", "test-engineer", "code-reviewer"],
        "expected_skills": ["skills/coding/csharp-idioms", "skills/testing/test-pyramid"],
        "execution_mode": "sequential",
        "final_reviewer": "code-reviewer"
    },
    "B": {
        "title": "Fix EF tracking issue",
        "stack": {"generation": "modern-dotnet", "orm": "ef-core"},
        "expected_agents": ["database-engineer", "test-engineer", "code-reviewer"],
        "expected_skills": ["skills/database/ef-diagnostics", "skills/engineering/evidence-first"],
        "execution_mode": "sequential",
        "final_reviewer": "code-reviewer"
    },
    "C": {
        "title": "Fix authentication bug",
        "stack": {"generation": "modern-dotnet", "framework": "aspnet-core"},
        "expected_agents": ["security-engineer", "dotnet-engineer", "test-engineer", "code-reviewer"],
        "expected_skills": ["skills/security/secure-by-default", "skills/security/secrets-audit"],
        "execution_mode": "hybrid",
        "final_reviewer": "code-reviewer"
    },
    "D": {
        "title": "Optimize slow SQL query",
        "stack": {"generation": "modern-dotnet", "orm": "dapper", "database": "sql-server"},
        "expected_agents": ["database-engineer", "performance-engineer", "test-engineer", "code-reviewer"],
        "expected_skills": ["skills/database/sql-safety", "skills/performance/allocation-profiling"],
        "execution_mode": "hybrid",
        "final_reviewer": "code-reviewer"
    },
    "E": {
        "title": "Modernize MVC 5 application",
        "stack": {"generation": "legacy-framework", "web": "mvc5"},
        "expected_agents": ["legacy-analyst", "migration-engineer", "test-engineer", "code-reviewer"],
        "expected_skills": ["skills/legacy/legacy-safety-guard", "skills/migration/incremental-upgrade"],
        "execution_mode": "sequential",
        "final_reviewer": "code-reviewer"
    },
    "F": {
        "title": "Add ABP permission",
        "stack": {"generation": "modern-dotnet", "abp": True},
        "expected_agents": ["dotnet-engineer", "test-engineer", "code-reviewer"],
        "expected_skills": ["skills/architecture/clean-boundaries", "skills/security/secure-by-default"],
        "execution_mode": "sequential",
        "final_reviewer": "code-reviewer"
    },
    "G": {
        "title": "Investigate legacy repository",
        "stack": {"generation": "legacy-framework", "has_wcf": True},
        "expected_agents": ["legacy-analyst", "project-profiler", "tech-lead"],
        "expected_skills": ["skills/project-analysis/legacy-discovery", "skills/engineering/evidence-first"],
        "execution_mode": "parallel",
        "final_reviewer": "tech-lead"
    },
    "H": {
        "title": "Perform code review",
        "stack": {"generation": "any"},
        "expected_agents": ["code-reviewer"],
        "expected_skills": ["skills/engineering/evidence-first", "skills/engineering/minimal-change"],
        "execution_mode": "single",
        "final_reviewer": "code-reviewer"
    }
}

class TestRoutingScenarios(unittest.TestCase):

    def test_all_scenarios(self):
        for scenario_key, scenario_data in SCENARIOS.items():
            with self.subTest(scenario=scenario_key, title=scenario_data["title"]):
                # Verify agent assignment
                self.assertGreater(len(scenario_data["expected_agents"]), 0)
                self.assertIn(scenario_data["final_reviewer"], scenario_data["expected_agents"])

                # Verify execution order and mode
                if scenario_data["execution_mode"] == "sequential":
                    self.assertEqual(scenario_data["expected_agents"][-1], "code-reviewer")
                elif scenario_data["execution_mode"] == "parallel":
                    self.assertIn("legacy-analyst", scenario_data["expected_agents"])
                    self.assertIn("project-profiler", scenario_data["expected_agents"])

                # Verify skills are properly categorized
                for sk in scenario_data["expected_skills"]:
                    self.assertTrue(sk.startswith("skills/"))

if __name__ == "__main__":
    unittest.main()
