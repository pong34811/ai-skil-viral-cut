# Viral Cut

ค้นหา วิเคราะห์ และคัดเลือกช่วงเวลาที่มีศักยภาพสูงจากไฟล์ไลฟ์สตรีม (.mp4) เพื่อนำไปตัดต่อเป็นคลิปสั้นและคลิปยาว

## โครงสร้าง vault

```
├── AGENTS.md              — Auto-update Obsidian instructions
├── agent_skills/
│   ├── References.md            — ตัวอย่างผลงานจริง ใช้อ้างอิง
│   ├── Skills.md                — ภาพรวม Skill, Output Schema
│   ├── WorkFlows.md             — ขั้นตอนการทำงาน 6 Step
│   ├── Viral-Cut-Detection.md   — เกณฑ์วิเคราะห์ 6 ด้าน + สูตรคะแนน + แหล่งอ้างอิง
│   ├── Rules.md                 — ข้อจำกัด, หลักเกณฑ์, Quality Checklist
│   ├── Personas.md              — ข้อมูลผู้ใช้งานเป้าหมาย
│   ├── contents.md              — ตารางข้อมูลเกมทั้งหมด
│   ├── plan.md                  — Checklist ปฏิบัติการ
│   └── TROUBLESHOOTING.md       — ปัญหาที่พบบ่อย + วิธีแก้
├── scripts/
│   ├── export_viral_cuts.py — Export Excel
│   └── transcribe.py      — ถอดเสียงด้วย Groq API
├── .env                   — API keys (ไม่เข้า git)
├── raw/                   — วางไฟล์ .mp4 ที่นำเข้า
├── outputs/               — ไฟล์ผลลัพธ์ .xlsx
├── references/            — ข้อมูลอ้างอิงแบ่งตามวันที่
│   └── YYYY-MM-DD/
│       └── viral-cut-YYYY-MM-DD.xlsx
├── contents/                  — ข้อมูลเกมสำหรับอ้างอิง
│   ├── Arena of Valor.md
│   ├── Castle Crashers.md
│   ├── Cheese Rolling.md
│   ├── Minecraft.md
│   └── TEMPLATE.md            — แม่แบบสำหรับเกมใหม่
├── docs/
│   └── superpowers/specs/     — Design documents
├── example.txt                — Template prompt สำหรับเริ่มงาน
├── CHANGELOG.md               — ประวัติการเปลี่ยนแปลง
├── Welcome.md                 — หน้าแรกของ vault
└── AGENTS.md                  — Auto-update Obsidian instructions
```

## สถานะล่าสุด (2026-06-30)

### ✅ Project Audit & Fixes (23 issues)
✅ แก้ broken wiki link `[[scripts/Scripts]]` → `[[scripts/transcribe]]` + `[[scripts/export_viral_cuts]]`
✅ แก้ `scripts/.env` → `.env` ใน `plan.md`
✅ แก้ `Subtitle 1.srt` → ชื่อจริงใน 3 reference .md
✅ แก้เลข AGENTS.md (4→6 → 4→5)
✅ แก้ README.md: tree, casing, step numbers
✅ แก้ WorkFlows.md: indent, Chinese char `转录`, broken link
✅ แก้ transcribe.py: hardcoded path, ffmpeg/ffprobe error handling, .mp4 validation, API retry
✅ สร้าง `requirements.txt` + `.env.example`
✅ แก้ "การจอ" → "การ์ดจอ" ใน reference MD
✅ เก็บ `outputs/` + `references/` ไว้ตามที่ขอ

### ✅ Auto-Obsidian Update (AGENTS.md)
✅ สร้าง `AGENTS.md` — AI อัปเดตไฟล์ Obsidian อัตโนมัติหลังทำงานเสร็จทุกครั้ง
✅ แก้ไข path ใน AGENTS.md: `chat-history.md` → `agent_skills/chat-history.md`, `plan.md` → `agent_skills/plan.md`
✅ อัปเดต Welcome.md tree structure + wikilink ไปยัง AGENTS.md
✅ สร้าง design doc ที่ `docs/superpowers/specs/2026-06-17-auto-obsidian-update-design.md`
✅ ลบ `agent_skills/chat-history.md` (ใช้ superpowers แทนแล้ว)

### Minecraft Murder/Bed Wars (ล่าสุด — 2026-06-30)
✅ ถอดเสียง Groq Whisper (1425 segments, 83:33 นาที, 9 chunks)
✅ ตรวจทานคำผิด SRT (ธนู, เมอร์เดอร์, ชื่อผู้เล่น)
✅ วิเคราะห์ 6 Viral Cuts → ปรับเหลือ 4 Cuts (ลบ #1–3, เพิ่ม "อิมพอดเตอร์ก็ไม่เท่าไร")
✅ Export → `outputs/viral-cut-2026-06-30.xlsx`
✅ สร้าง `contents/Minecraft.md`
✅ อัปเดต `References.md`, `contents.md`

### Cheese Rolling collab
✅ ถอดเสียง Groq (1510 segments, 98.85 นาที)
✅ ตรวจทานคำผิด SRT
✅ วิเคราะห์ 5 Viral Cuts
✅ Export → `outputs/viral-cut-2026-06-17.xlsx`
✅ สร้าง `contents/Cheese Rolling.md`
✅ อัปเดต `References.md`

### ลบตัวละคร Elsword (Reference clip)
✅ ตรวจทานคำผิด SRT
✅ สร้าง MD ตัวอย่าง → `references/2026-06-16/ลบตัวละคร Elsword/`
✅ อัปเดต `References.md`

### Garena RoV Thailand #006
✅ ถอดเสียง → `.srt` + `.json`
✅ ตรวจทานคำผิด SRT
✅ วิเคราะห์ 4 Viral Cuts
✅ Export → `outputs/viral-cut-2026-06-11.xlsx`
✅ สร้าง `contents/arena of valor.md`

### Castle Crashers
✅ ถอดเสียง → `.srt` + `.json`
✅ วิเคราะห์ 5 Viral Cuts (1-3 นาที)
✅ Export → `outputs/viral-cut-2026-06-10.xlsx`

---

## เริ่มต้น
0. ดู [[AGENTS]] สำหรับพฤติกรรม AI ในการอัปเดตไฟล์อัตโนมัติ
1. วางไฟล์ `.mp4` ใน `raw/`
2. รัน `python scripts/transcribe.py` เพื่อถอดเสียง
3. เปิด [[agent_skills/Skills]] เพื่อดูเกณฑ์การวิเคราะห์
4. ดู [[agent_skills/WorkFlows]] สำหรับขั้นตอน
5. ตรวจสอบ [[agent_skills/Rules]] สำหรับข้อควรระวัง
6. ดู [[agent_skills/References]] สำหรับตัวอย่างผลงานที่ผ่านมา
7. ดู [[agent_skills/TROUBLESHOOTING]] เมื่อเจอปัญหา
8. ใช้ [[scripts/transcribe]] สำหรับถอดเสียง และ [[scripts/export_viral_cuts]] สำหรับ Export ผลลัพธ์
9. ดู [[CHANGELOG]] สำหรับประวัติการเปลี่ยนแปลง