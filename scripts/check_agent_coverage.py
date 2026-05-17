#!/usr/bin/env python3
"""Check which projects can see BeastMode custom agents.

This script scans projects under a root folder and reports whether each project
is fully covered by shared BeastMode custom agents, considering global and
workspace-level VS Code settings.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def count_agent_files(folder: Path) -> int:
    if not folder.exists() or not folder.is_dir():
        return 0
    return sum(1 for p in folder.glob("*.agent.md") if p.is_file())


def read_text_if_exists(path: Path) -> str:
    if not path.exists() or not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def has_agent_disabled(settings_text: str) -> bool:
    return bool(re.search(r'"chat\.agent\.enabled"\s*:\s*false', settings_text))


def has_agent_enabled(settings_text: str) -> bool:
    return bool(re.search(r'"chat\.agent\.enabled"\s*:\s*true', settings_text))


def has_agent_locations_key(settings_text: str) -> bool:
    return '"chat.agentFilesLocations"' in settings_text


def includes_path(settings_text: str, path: Path) -> bool:
    norm = str(path)
    return norm in settings_text


def project_dirs(projects_root: Path) -> list[Path]:
    if not projects_root.exists():
        return []
    dirs = []
    for child in sorted(projects_root.iterdir()):
        if not child.is_dir():
            continue
        if child.name.startswith("."):
            continue
        dirs.append(child)
    return dirs


def main() -> int:
    parser = argparse.ArgumentParser(description="Check BeastMode custom-agent coverage across projects")
    parser.add_argument("--projects-root", default="/home/kevin/Projects", help="Root folder containing projects")
    parser.add_argument("--beastmode-root", default="/home/kevin/Projects/BeastMode", help="BeastMode repository root")
    parser.add_argument(
        "--user-settings",
        default="/home/kevin/.config/Code/User/settings.json",
        help="VS Code user settings path",
    )
    parser.add_argument(
        "--user-agents-dir",
        default="/home/kevin/.copilot/agents",
        help="Built-in user-level custom agents directory",
    )
    args = parser.parse_args()

    projects_root = Path(args.projects_root)
    beastmode_root = Path(args.beastmode_root)
    user_settings_path = Path(args.user_settings)
    user_agents_dir = Path(args.user_agents_dir)

    beast_agents_dir = beastmode_root / ".github" / "agents"
    expected_agents = count_agent_files(beast_agents_dir)
    user_agents = count_agent_files(user_agents_dir)

    user_settings = read_text_if_exists(user_settings_path)
    user_enabled = has_agent_enabled(user_settings)
    user_has_beast_path = includes_path(user_settings, beast_agents_dir)

    global_ready = expected_agents > 0 and user_agents >= expected_agents and user_enabled
    settings_hint_ok = user_enabled and user_has_beast_path

    updated: list[tuple[str, str]] = []
    blocked: list[tuple[str, str]] = []

    for proj in project_dirs(projects_root):
        if proj.resolve() == beastmode_root.resolve():
            continue

        settings_file = proj / ".vscode" / "settings.json"
        settings_text = read_text_if_exists(settings_file)

        if settings_text and has_agent_disabled(settings_text):
            blocked.append((proj.name, "workspace sets chat.agent.enabled=false"))
            continue

        if settings_text and has_agent_locations_key(settings_text):
            if includes_path(settings_text, beast_agents_dir):
                updated.append((proj.name, "workspace includes BeastMode agent path"))
            else:
                blocked.append((proj.name, "workspace overrides chat.agentFilesLocations without BeastMode path"))
            continue

        if global_ready:
            updated.append((proj.name, "inherits global user agents (~/.copilot/agents)"))
        elif settings_hint_ok:
            updated.append((proj.name, "inherits user settings path to BeastMode agents"))
        else:
            blocked.append((proj.name, "global user agent discovery not fully configured"))

    print("BeastMode Custom Agent Coverage Report")
    print("=" * 40)
    print(f"Projects root: {projects_root}")
    print(f"BeastMode agents dir: {beast_agents_dir}")
    print(f"Expected agents: {expected_agents}")
    print(f"User agents dir: {user_agents_dir}")
    print(f"User agents found: {user_agents}")
    print(f"User settings enabled: {user_enabled}")
    print(f"User settings include BeastMode path: {user_has_beast_path}")
    print(f"Global readiness: {global_ready}")
    print()

    print(f"UPDATED ({len(updated)} projects)")
    print("-" * 40)
    for name, reason in updated:
        print(f"- {name}: {reason}")

    print()
    print(f"NEEDS UPDATE ({len(blocked)} projects)")
    print("-" * 40)
    for name, reason in blocked:
        print(f"- {name}: {reason}")

    return 0 if not blocked else 2


if __name__ == "__main__":
    raise SystemExit(main())
