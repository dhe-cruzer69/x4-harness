# x4-harness

**Multi-agent harness for coordinating coding agents** (Claude Code, Codex, Pi, and others) with shared context, role assignment, and adaptive memory.

Part of the X4 / ARIEX4Ops ecosystem — local-first, evidence-first.

## Why

Modern agent fleets need a thin, reliable coordination layer that:

- assigns roles (planner, implementer, reviewer, security)
- shares a single source of truth for context
- recovers when a specialist fails
- records evidence of every hand-off

## Quick Start

```bash
pip install -e ".[dev]"
python -m x4_harness.cli init my-team
```

<!-- X4-APEX-DIAGRAM-START:x4-harness -->

```mermaid
flowchart TD
    TEAM[Team Configuration] --> ROLES[Role and Capability Contracts]
    ROLES --> DISPATCH[Coordinator Dispatch]
    DISPATCH --> SPECIALIST[Planner / Implementer / Reviewer / Security Agent]
    SPECIALIST --> HANDOFF[Evidence-backed Handoff]
    HANDOFF --> SCHEMA[Validate Payload and Ownership]
    SCHEMA -->|valid| MEMORY[Shared Context and Memory]
    SCHEMA -->|invalid| REJECT[Reject Handoff]
    MEMORY --> REVIEW[Supervisor Review]
    REVIEW -->|accepted| RESULT[Record Result and Evidence]
    REVIEW -->|recoverable failure| RETRY[Bounded Retry or Reassignment]
    RETRY --> DISPATCH
    REVIEW -->|timeout or cancellation| STOP[Stop and Report]
```

<!-- X4-APEX-DIAGRAM-END:x4-harness -->

## Core Concepts

| Concept | Description |
|---------|-------------|
| Team | Named group of agent slots |
| Role | Capability contract (tools + system prompt + limits) |
| Shared Memory | Ephemeral + persistent store visible to all members |
| Handoff | Evidence-backed transfer of ownership |

## License

Apache-2.0
