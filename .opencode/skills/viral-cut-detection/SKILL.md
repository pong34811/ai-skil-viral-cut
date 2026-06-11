---
name: viral-cut-detection
description: >
  Detect viral moments from livestream .mp4 files. Transcribe with Groq (Whisper),
  score segments on 6 criteria (Emotion, Chaos, Humor, Interaction, PlotTwist,
  Educational), rank by weighted formula, export to Excel timestamped by UTC date.
  See agent_skills/ for full reference.
---

## Overview

Viral Cut Detector analyzes livestream `.mp4` files to find and rank the most engaging segments (1-3 min each) for short-form content.

## Workflow (6 Steps)

1. **Receive** — user places `.mp4` in `raw/`, provides title + metadata
2. **Transcribe** — `python scripts/transcribe.py raw/<file>.mp4 --srt --json` (Groq Whisper, auto-chunks >25MB)
3. **Score** — rate each segment 1-10 on 6 criteria, compute weighted total
4. **Select** — rank by score, enforce min thresholds (≥6.0 short-form / ≥5.0 long-form), deduplicate overlaps
5. **Output** — format per Output Schema (Category, Title, Start/End time HH:MM:SS, Filename, Duration)
6. **Export** — `export_all(cuts)` → `outputs/viral-cut-YYYY-MM-DD.xlsx`, copy to `references/YYYY-MM-DD/`

## Scoring Formula

```python
score = (emotion * 0.20) + (chaos * 0.20) + (humor * 0.20) + (interaction * 0.15) + (plot_twist * 0.15) + (educational * 0.10)
```

## Key Rules

- Each cut **≥ 40 seconds**; expand context if shorter
- **No overlapping** timelines; merge if < 30 s apart
- No cut below score threshold (6.0 short / 5.0 long)
- Tie-breaker priority: Chaos > Humor > Interaction
- Content constraints: no copyrighted, illegal, hateful, or doxxing material
- Update `Welcome.md` after every completed task
- **Do NOT use git** unless the user explicitly asks

## Tools

- `scripts/transcribe.py` — Groq speech-to-text
- `scripts/export_viral_cuts.py` — Excel export
- FFmpeg — audio extraction, video analysis
- `.env` — stores `GROQ_API_KEY`

## References

See `agent_skills/` for full Skills, WorkFlows, Rules, and Viral-Cut-Detection docs.
