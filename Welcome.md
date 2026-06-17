# Viral Cut

ค้นหา วิเคราะห์ และคัดเลือกช่วงเวลาที่มีศักยภาพสูงจากไฟล์ไลฟ์สตรีม (.mp4) เพื่อนำไปตัดต่อเป็นคลิปสั้นและคลิปยาว

## โครงสร้าง vault

```
├── agent_skills/
│   ├── References.md            — ตัวอย่างผลงานจริง ใช้อ้างอิง
│   ├── Skills.md                — ภาพรวม Skill, Output Schema
│   ├── WorkFlows.md             — ขั้นตอนการทำงาน 6 Step
│   ├── Viral-Cut-Detection.md   — เกณฑ์วิเคราะห์ 6 ด้าน + สูตรคะแนน + แหล่งอ้างอิง
│   └── Rules.md                 — ข้อจำกัด, หลักเกณฑ์, Quality Checklist
├── scripts/
│   ├── Scripts.md         — เอกสารการใช้งาน script
│   ├── export_viral_cuts.py — Export Excel
│   └── transcribe.py      — ถอดเสียงด้วย Groq API
├── .env                   — API keys (ไม่เข้า git)
├── raw/                   — วางไฟล์ .mp4 ที่นำเข้า
├── outputs/               — ไฟล์ผลลัพธ์ .xlsx
├── references/            — ข้อมูลอ้างอิงแบ่งตามวันที่
│   └── YYYY-MM-DD/
│       └── viral-cut-YYYY-MM-DD.xlsx
└── Welcome.md
```

## สถานะล่าสุด (2026-06-17)

### Cheese Rolling collab (ล่าสุด)
✅ ถอดเสียง Groq (1510 segments, 98.85 นาที)
✅ ตรวจทานคำผิด SRT
✅ วิเคราะห์ 5 Viral Cuts
✅ Export → `outputs/viral-cut-2026-06-17.xlsx`
✅ สร้าง `contents/Cheese Rolling.md`
✅ อัปเดต `References.md` + `chat-history.md`

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
1. วางไฟล์ `.mp4` ใน `raw/`
2. รัน `python scripts/transcribe.py` เพื่อถอดเสียง
3. เปิด [[agent_skills/Skills]] เพื่อดูเกณฑ์การวิเคราะห์
4. ดู [[agent_skills/WorkFlows]] สำหรับขั้นตอน
5. ตรวจสอบ [[agent_skills/Rules]] สำหรับข้อควรระวัง
6. ดู [[agent_skills/References]] สำหรับตัวอย่างผลงานที่ผ่านมา
7. ใช้ [[scripts/Scripts]] สำหรับ Export ผลลัพธ์