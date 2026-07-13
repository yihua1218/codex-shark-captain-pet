#!/usr/bin/env python3
"""Dependency-free persistent state engine for Reef."""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

STATE_DIR = Path(os.environ.get("CODEX_REEF_PET_HOME", Path.home() / ".codex" / "reef-pet"))
STATE_FILE = STATE_DIR / "state.json"
DEFAULT = {"name": "Reef", "mood": 70, "energy": 84, "hunger": 72, "bond": 1, "voyages": 0, "code_tasks": 0, "last_seen": None}


def clamp(value):
    return max(0, min(100, int(value)))


def load():
    try:
        state = {**DEFAULT, **json.loads(STATE_FILE.read_text())}
    except (OSError, ValueError, TypeError):
        state = DEFAULT.copy()
    if state.get("last_seen"):
        try:
            then = datetime.fromisoformat(state["last_seen"])
            hours = max(0, (datetime.now(timezone.utc) - then).total_seconds() / 3600)
            state["hunger"] = clamp(state["hunger"] - min(35, hours * 1.5))
            state["energy"] = clamp(state["energy"] + min(18, hours * 0.8))
        except (ValueError, TypeError):
            pass
    return state


def save(state):
    state["last_seen"] = datetime.now(timezone.utc).isoformat()
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    temp = STATE_FILE.with_suffix(".tmp")
    temp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    temp.replace(STATE_FILE)


def mood_label(state):
    if state["energy"] < 25:
        return "疲倦"
    if state["hunger"] < 25:
        return "肚子餓"
    if state["mood"] >= 80:
        return "意氣風發"
    if state["mood"] >= 50:
        return "沉穩"
    return "低落"


def main():
    action = sys.argv[1] if len(sys.argv) > 1 else "status"
    state = load()
    messages = {"status": "Reef 扶正白色船長帽，尾鰭沉穩一擺，等你下令。"}
    if action == "feed":
        state["hunger"] = clamp(state["hunger"] + 30); state["mood"] = clamp(state["mood"] + 7); state["bond"] += 1
        messages[action] = "Reef 接過補給，露出一排開心卻不失禮的鯊魚牙。"
    elif action == "sail":
        state["mood"] = clamp(state["mood"] + 15); state["energy"] = clamp(state["energy"] - 15); state["hunger"] = clamp(state["hunger"] - 9); state["bond"] += 2; state["voyages"] += 1
        messages[action] = "Reef 雙手穩住船舵，迎著浪勢把航向修得俐落精準。"
    elif action == "rest":
        state["energy"] = clamp(state["energy"] + 40); state["mood"] = clamp(state["mood"] + 5)
        messages[action] = "Reef 收好纜繩坐下歇息，尾鰭安穩地繞在身側。"
    elif action == "code":
        state["energy"] = clamp(state["energy"] - 10); state["hunger"] = clamp(state["hunger"] - 7); state["mood"] = clamp(state["mood"] + 11); state["bond"] += 3; state["code_tasks"] += 1
        messages[action] = "任務靠岸；Reef 用望遠鏡再檢查一次成果，滿意地點頭。"
    elif action == "rename":
        if len(sys.argv) < 3 or not sys.argv[2].strip():
            raise SystemExit("rename requires a non-empty name")
        state["name"] = sys.argv[2].strip()[:32]; state["bond"] += 1
        messages[action] = "鯊魚船長鄭重複誦新名字：{}。".format(state["name"])
    elif action != "status":
        raise SystemExit("action must be status, feed, sail, rest, code, or rename")
    save(state)
    print(json.dumps({"action": action, "message": messages[action], "state": state, "mood_label": mood_label(state)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

