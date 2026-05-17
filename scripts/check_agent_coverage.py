#!/usr/bin/env python3
"""Check which projects can see BeastMode custom agents.

This script scans projects under a root folder and reports whether each project
is fully covered by shared BeastMode custom agents, considering global and
workspace-level VS Code settings.
"""

from __future__ import annotations

import argparse
import json
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


def strip_jsonc_comments(text: str) -> str:
    out: list[str] = []
    i = 0
    in_string = False
    escaped = False
    while i < len(text):
        ch = text[i]

        if in_string:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            i += 1
            continue

        if ch == '"':
            in_string = True
            out.append(ch)
            i += 1
            continue

        if ch == "/" and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt == "/":
                i += 2
                while i < len(text) and text[i] != "\n":
                    i += 1
                continue
            if nxt == "*":
                i += 2
                while i + 1 < len(text) and not (text[i] == "*" and text[i + 1] == "/"):
                    i += 1
                i += 2
                continue

        out.append(ch)
        i += 1

    return "".join(out)


def strip_trailing_commas(text: str) -> str:
    out: list[str] = []
    i = 0
    in_string = False
    escaped = False
    length = len(text)

    while i < length:
        ch = text[i]

        if in_string:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            i += 1
            continue

        if ch == '"':
            in_string = True
            out.append(ch)
            i += 1
            continue

        if ch == ",":
            j = i + 1
            while j < length and text[j] in " \t\r\n":
                j += 1
            if j < length and text[j] in "]}":
                i += 1
                continue

        out.append(ch)
        i += 1

    return "".join(out)


def sanitize_jsonc(text: str) -> str:
    no_comments = strip_jsonc_comments(text)
    return strip_trailing_commas(no_comments)


def load_json_file(path: Path) -> tuple[dict, str]:
    text = read_text_if_exists(path)
    if not text:
        return {}, ""
    try:
        parsed = json.loads(text)
    except Exception as exc:  # noqa: BLE001
        try:
            parsed = json.loads(sanitize_jsonc(text))
        except Exception:  # noqa: BLE001
            return {}, str(exc)
    if isinstance(parsed, dict):
        return parsed, ""
    return {}, "settings root is not a JSON object"


def write_json_file(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=4, sort_keys=False) + "\n", encoding="utf-8")


def ensure_beastmode_locations(data: dict, beast_agents_dir: Path) -> bool:
    key = "chat.agentFilesLocations"
    beast_path = str(beast_agents_dir)
    current = data.get(key)

    if isinstance(current, dict):
        if current.get(beast_path) is True:
            return False
        current[beast_path] = True
        data[key] = current
        return True

    if isinstance(current, list):
        if beast_path in current:
            return False
        current.append(beast_path)
        data[key] = current
        return True

    data[key] = {beast_path: True}
    return True


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
    parser.add_argument(
        "--autofix",
        action="store_true",
        help="Auto-fix workspace settings that override chat.agentFilesLocations without BeastMode path",
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
    to_fix: list[tuple[Path, str]] = []

    for proj in project_dirs(projects_root):
        if proj.resolve() == beastmode_root.resolve():
            continue

        settings_file = proj / ".vscode" / "settings.json"
        settings_text = read_text_if_exists(settings_file)

        if settings_text and has_agent_disabled(settings_text):
            reason = "workspace sets chat.agent.enabled=false"
            blocked.append((proj.name, reason))
            to_fix.append((proj, reason))
            continue

        if settings_text and has_agent_locations_key(settings_text):
            if includes_path(settings_text, beast_agents_dir):
                updated.append((proj.name, "workspace includes BeastMode agent path"))
            else:
                reason = "workspace overrides chat.agentFilesLocations without BeastMode path"
                blocked.append((proj.name, reason))
                to_fix.append((proj, reason))
            continue

        if global_ready:
            updated.append((proj.name, "inherits global user agents (~/.copilot/agents)"))
        elif settings_hint_ok:
            updated.append((proj.name, "inherits user settings path to BeastMode agents"))
        else:
            blocked.append((proj.name, "global user agent discovery not fully configured"))

    fixed: list[tuple[str, str]] = []
    fix_failed: list[tuple[str, str]] = []

    if args.autofix and to_fix:
        for proj, reason in to_fix:
            settings_file = proj / ".vscode" / "settings.json"
            data, err = load_json_file(settings_file)
            if err:
                fix_failed.append((proj.name, f"parse error: {err}"))
                continue

            changed = False
            if reason == "workspace sets chat.agent.enabled=false":
                if data.get("chat.agent.enabled") is False:
                    data["chat.agent.enabled"] = True
                    changed = True

            if ensure_beastmode_locations(data, beast_agents_dir):
                changed = True

            if changed:
                write_json_file(settings_file, data)
                fixed.append((proj.name, "updated .vscode/settings.json"))
            else:
                fixed.append((proj.name, "already compliant after parse"))

        if fixed:
            updated_names = {name for name, _ in updated}
            for name, _ in fixed:
                if name not in updated_names:
                    updated.append((name, "autofix applied"))
                    updated_names.add(name)

            blocked = [(name, reason) for name, reason in blocked if name not in updated_names]

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

    if args.autofix:
        print(f"AUTOFIX ATTEMPTED: {len(to_fix)}")
        print(f"AUTOFIX APPLIED: {len(fixed)}")
        print(f"AUTOFIX FAILED: {len(fix_failed)}")
        for name, reason in fix_failed:
            print(f"- autofix failed {name}: {reason}")
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

    return 0 if not blocked and not fix_failed else 2


if __name__ == "__main__":
    raise SystemExit(main())
