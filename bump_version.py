#!/usr/bin/env python

import subprocess
import sys
import re
from pathlib import Path
import tomlkit

PYPROJECT_PATH = Path("pyproject.toml")

def get_current_version():
    content = PYPROJECT_PATH.read_text(encoding="utf-8")
    data = tomlkit.parse(content)
    return data["project"]["version"]

def bump_version(current, part):
    major, minor, patch = map(int, current.split("."))

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError("Invalid bump type. Use: major, minor, patch")

    return f"{major}.{minor}.{patch}"

def update_pyproject(new_version):
    content = PYPROJECT_PATH.read_text(encoding="utf-8")
    data = tomlkit.parse(content)
    data["project"]["version"] = new_version
    PYPROJECT_PATH.write_text(tomlkit.dumps(data), encoding="utf-8")

def run_cmd(cmd):
    print(f"👉 {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["major", "minor", "patch"]:
        print("Usage: python bump_version.py [major|minor|patch]")
        sys.exit(1)

    part = sys.argv[1]
    current = get_current_version()
    new_version = bump_version(current, part)

    print(f"📦 Bumping version: {current} → {new_version}")
    update_pyproject(new_version)

    run_cmd(f'git add {PYPROJECT_PATH}')
    run_cmd(f'git commit -m "🔖 Bump version to {new_version}"')
    run_cmd(f'git tag v{new_version}')
    run_cmd('git push')
    run_cmd('git push --tags')
    print(f"✅ Version bumped to {new_version} and tagged as v{new_version}")

if __name__ == "__main__":
    main()
