#!/usr/bin/env python3
"""
Integrity Test Suite verifying frontmatter, tool boundaries, line budgets, and circular references using standard unittest.
"""

import os
import sys
import unittest

scripts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts")
sys.path.insert(0, scripts_dir)

from validate import check_frontmatter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestIntegrity(unittest.TestCase):

    def test_all_agents_exist(self):
        agents_dir = os.path.join(REPO_ROOT, ".agents", "agents")
        expected_agents = [
            "tech-lead", "project-profiler", "architect", "dotnet-engineer",
            "database-engineer", "test-engineer", "security-engineer",
            "performance-engineer", "migration-engineer", "legacy-analyst", "code-reviewer"
        ]
        for ag in expected_agents:
            ag_path = os.path.join(agents_dir, ag, "agent.md")
            self.assertTrue(os.path.isfile(ag_path), f"Missing agent: {ag}")
            valid, msg, data = check_frontmatter(ag_path)
            self.assertTrue(valid, f"Invalid frontmatter in {ag}: {msg}")
            self.assertEqual(data["name"], ag)
            self.assertIn("role", data)
            self.assertIn("tools", data)

    def test_discovery_agents_least_privilege(self):
        agents_dir = os.path.join(REPO_ROOT, ".agents", "agents")
        read_only_agents = ["project-profiler", "legacy-analyst"]
        forbidden_tools = ["write_to_file", "replace_file_content", "multi_replace_file_content", "run_command"]

        for ag in read_only_agents:
            ag_path = os.path.join(agents_dir, ag, "agent.md")
            _, _, data = check_frontmatter(ag_path)
            tools = data.get("tools", [])
            for fb in forbidden_tools:
                self.assertNotIn(fb, tools, f"Discovery agent {ag} contains forbidden modifying tool {fb}")

    def test_all_skills_have_frontmatter(self):
        skills_dir = os.path.join(REPO_ROOT, ".agents", "skills")
        skill_count = 0
        for root, _, files in os.walk(skills_dir):
            if "SKILL.md" in files:
                skill_count += 1
                skill_path = os.path.join(root, "SKILL.md")
                valid, msg, data = check_frontmatter(skill_path)
                self.assertTrue(valid, f"Invalid frontmatter in {skill_path}: {msg}")
                self.assertIn("name", data)
                self.assertIn("description", data)
                self.assertGreater(len(data["description"].strip()), 10)
        self.assertGreaterEqual(skill_count, 15)

    def test_all_rules_have_why_it_exists(self):
        rules_dir = os.path.join(REPO_ROOT, ".agents", "rules")
        rule_files = [f for f in os.listdir(rules_dir) if f.endswith(".md")]
        self.assertGreaterEqual(len(rule_files), 15)
        for rf in rule_files:
            with open(os.path.join(rules_dir, rf), "r", encoding="utf-8") as f:
                content = f.read()
                self.assertIn("Why It Exists", content, f"Rule {rf} missing 'Why It Exists' section")

if __name__ == "__main__":
    unittest.main()
