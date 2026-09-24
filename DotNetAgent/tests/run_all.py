#!/usr/bin/env python3
"""
Unified Cross-Platform Test Runner for Universal .NET AI Core Team.
Runs:
1. Validation suite (scripts/validate.py)
2. All unittest test cases in tests/
3. Independent audit check (scripts/audit.py)
"""

import os
import sys
import unittest

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scripts_dir = os.path.join(repo_root, "scripts")
    tests_dir = os.path.join(repo_root, "tests")

    sys.path.insert(0, scripts_dir)
    sys.path.insert(0, tests_dir)

    print("=" * 60)
    print("UNIVERSAL .NET AI CORE TEAM: COMPREHENSIVE TEST RUNNER")
    print("=" * 60)

    # 1. Run validate.py
    from validate import run_validation
    print("\n--- PHASE 1: STRUCTURAL INTEGRITY VALIDATION ---")
    try:
        run_validation(repo_root)
    except SystemExit as e:
        if e.code != 0:
            print("[FAIL] Structural integrity validation failed!")
            sys.exit(1)

    # 2. Run unittests
    print("\n--- PHASE 2: UNIT TESTS & FIXTURE PROFILING ---")
    loader = unittest.TestLoader()
    suite = loader.discover(tests_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        print(f"\n[FAIL] Unit tests failed: {len(result.failures)} failures, {len(result.errors)} errors.")
        sys.exit(1)

    # 3. Run audit.py
    print("\n--- PHASE 3: ARCHITECTURAL AUDIT GATE ---")
    from audit import audit_repository
    audit_report = audit_repository(repo_root)
    if audit_report["CRITICAL"] or audit_report["HIGH"]:
        print(f"[FAIL] Audit gate detected critical/high issues!")
        sys.exit(1)
    else:
        print("[OK] Audit gate clean: 0 Critical, 0 High issues.")

    print("\n" + "=" * 60)
    print("ALL TEST PHASES & GATES PASSED CLEANLY! CORE TEAM VERIFIED.")
    print("=" * 60)
    sys.exit(0)

if __name__ == "__main__":
    main()
