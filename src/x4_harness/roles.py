"""Role definitions for the harness."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class Role:
    name: str
    description: str
    tools: List[str] = field(default_factory=list)
    max_turns: int = 20
    autonomy_level: int = 1  # 0-3 X4 policy


DEFAULT_ROLES = {
    "planner": Role("planner", "Decomposes goals into tasks", tools=["read", "search"], autonomy_level=1),
    "implementer": Role("implementer", "Writes and edits code", tools=["read", "write", "exec"], autonomy_level=1),
    "reviewer": Role("reviewer", "Reviews diffs and evidence", tools=["read", "comment"], autonomy_level=0),
    "security": Role("security", "Scans for secrets and policy violations", tools=["read", "scan"], autonomy_level=0),
}
