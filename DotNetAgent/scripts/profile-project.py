#!/usr/bin/env python3
"""Wrapper forwarding to profile_project.py"""
import runpy
import sys

if __name__ == "__main__":
    runpy.run_module("profile_project", run_name="__main__")
