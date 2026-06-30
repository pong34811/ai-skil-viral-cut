# Changelog

> ประวัติการเปลี่ยนแปลงทั้งหมดของโปรเจกต์ Viral Cut Detection

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
