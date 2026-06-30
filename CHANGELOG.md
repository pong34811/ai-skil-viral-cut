# Changelog

> ประวัติการเปลี่ยนแปลงทั้งหมดของโปรเจกต์ Viral Cut Detection

---

## 2026-06-30 — ตัดคลิป + Fix ffmpeg auto-detect

### Added
- `scripts/cut_clips.py` — auto-detect ffmpeg path (WinGet), `errors="replace"` fix Windows UnicodeDecodeError
- ตัดคลิป Minecraft 4 คลิป → `outputs/2026-06-30/clips/`

### Changed
- เปลี่ยน output structure: `outputs/YYYY-MM-DD/viral-cut-YYYY-MM-DD.xlsx` + `clips/`
- Docs: plan.md, WorkFlows.md, README.md, Welcome.md, Rules.md, Personas.md, SKILL.md paths

---

## 2026-06-30 — ปรับ Viral Cuts Minecraft ตามคำขอ

### Changed
- ลบ Cuts #1–3 (ไม่น่าสนใจ)
- เพิ่ม Cut ใหม่ "อิมพอดเตอร์ก็ไม่เท่าไร" (00:12:00–00:12:50, คะแนน 6.25)
- ตัดเหลือ 4 Cuts เรียงตามคะแนน

---

## 2026-06-30 — Minecraft Pipeline + Code Review Fixes

### Added
- `contents/Minecraft.md` — ข้อมูลเกม Minecraft
- `contents/TEMPLATE.md` — แม่แบบสำหรับสร้างข้อมูลเกมใหม่
- `agent_skills/TROUBLESHOOTING.md` — ปัญหาที่พบบ่อย + วิธีแก้
- `CHANGELOG.md` — ไฟล์นี้

### Changed
- ปรับชื่อไฟล์เกมเป็น Pascal Case: `arena of valor` → `Arena of Valor`, `castle crashers` → `Castle Crashers`
- อัปเดตลิงก์ Wiki Link ทุกจุดให้ตรงกับชื่อไฟล์ใหม่
- `Skills.md` — อัปเดต Output Schema รวมคอลัมน์คะแนน Viral
- `Rules.md` §6 — ปรับปรุงข้อกำหนด Output Format รองรับคะแนน Viral
- `contents.md` — อัปเดตวิธีเพิ่มเกมใหม่ (ใช้ TEMPLATE.md)
- `Welcome.md` — อัปเดต tree structure, เพิ่มสถานะ Minecraft
- `plan.md` — tick `[x]` Step 3, 4, 5 sub-items
- `export_viral_cuts.py` — เพิ่มคอลัมน์ "คะแนน Viral"
- `.gitignore` — เพิ่ม `references/`

### Fixed
- Code Review: Chinese characters → Thai ใน Minecraft.md
- Code Review: "Eragon" → "Ender Dragon" ใน Minecraft.md
- Code Review: เรียง cut ตามคะแนน descending ใน References.md
- Code Review: references/ ไม่ถูกละเว้นใน .gitignore

---

## 2026-06-17 — Cheese Rolling Pipeline + Auto-Obsidian Update

### Added
- `AGENTS.md` — Auto-update Obsidian instructions
- `docs/superpowers/specs/2026-06-17-auto-obsidian-update-design.md`
- `contents/Cheese Rolling.md`
- `requirements.txt`, `.env.example`

### Changed
- แก้ broken wiki links ทั่วโปรเจกต์ (23 issues)
- `transcribe.py` — hardcoded path, ffmpeg error handling, .mp4 validation, API retry
- `README.md` — tree, casing, step numbers
- `WorkFlows.md` — indent, broken link
- `Welcome.md` — tree structure + wikilinks

### Removed
- `agent_skills/chat-history.md`

---

## 2026-06-16 — Elsword Reference Clip

### Added
- `references/2026-06-16/ลบตัวละคร Elsword/` — Reference MD + SRT

---

## 2026-06-11 — Garena RoV Thailand #006

### Added
- `contents/Arena of Valor.md` (สร้างครั้งแรก, สะกด `arena of valor`)
- `outputs/viral-cut-2026-06-11.xlsx` (4 Viral Cuts)

---

## 2026-06-10 — Castle Crashers Pipeline (เริ่มต้น)

### Added
- `outputs/viral-cut-2026-06-10.xlsx` (5 Viral Cuts)
- `contents/castle crashers.md` (สร้างครั้งแรก, สะกด lowercase)
- เอกสาร agent_skills ทั้งหมด (Skills, Rules, WorkFlows, Viral-Cut-Detection, Personas, References, contents, plan)
- `scripts/transcribe.py`, `scripts/export_viral_cuts.py`
- `example.txt`
