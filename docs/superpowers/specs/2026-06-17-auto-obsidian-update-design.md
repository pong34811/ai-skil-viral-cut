# Auto-Obsidian Update Design

## Problem
Every time work completes in opencode, the user must manually type instructions to update Obsidian vault files. This is repetitive and slows down the workflow.

## Solution
Create `AGENTS.md` — a file that opencode reads automatically and follows as instructions. It tells the AI to auto-update all Obsidian files after every task completion, without waiting for the user to ask.

## Files auto-updated
| File | Update type |
|------|-------------|
| `Welcome.md` | Add/update latest project status section |
| `agent_skills/References.md` | Add new reference entries for new cuts/clips |
| `agent_skills/contents.md` | Add new game row when `contents/<game>.md` is created |
| `agent_skills/plan.md` | Tick `[x]` completed steps |
| `agent_skills/Personas.md` | Update Persona info if new data available |

## Consistency checks
- `contents/` directory vs `agent_skills/contents.md` — must match
- Links in `agent_skills/References.md` — must point to existing files
- Timestamp format: `HH:MM:SS` only
- Output filenames: UTC date (`YYYY-MM-DD`)

## Why AGENTS.md?
- Zero setup (just create the file)
- opencode has built-in support for AGENTS.md
- No external dependencies or scripts needed
- AI understands natural language instructions in it
- Changes take effect immediately on next task
