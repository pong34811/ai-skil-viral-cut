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

## สถานะล่าสุด (2026-06-10)

✅ **ถอดเสียง:** `raw/2789194443-194837833-1573b8fc-cffa-4faf-85ee-7ce7abe38671.mp4` → `.srt` + `.json`
✅ **วิเคราะห์:** พบ 6 Viral Cuts (คะแนน 5.8-7.4/10)
✅ **Export:** `outputs/viral-cut-2026-06-10.xlsx`
✅ **อ้างอิง:** อัปเดต [[agent_skills/References]] แล้ว

### Top Cuts
| # | เวลา | หมวด | คะแนน |
|---|------|------|:----:|
| 1 | 00:54:53 | Chaos โรบินฮูช | **7.4** |
| 2 | 00:19:08 | Chaos CPR | **7.4** |
| 3 | 00:08:36 | Plot Twist | **6.3** |
| 4 | 00:42:30 | Interaction | **6.1** |
| 5 | 00:34:40 | Humor | **5.9** |
| 6 | 01:09:15 | Emotion | **5.8** |

---

## เริ่มต้น
1. วางไฟล์ `.mp4` ใน `raw/`
2. รัน `python scripts/transcribe.py` เพื่อถอดเสียง
3. เปิด [[agent_skills/Skills]] เพื่อดูเกณฑ์การวิเคราะห์
4. ดู [[agent_skills/WorkFlows]] สำหรับขั้นตอน
5. ตรวจสอบ [[agent_skills/Rules]] สำหรับข้อควรระวัง
6. ดู [[agent_skills/References]] สำหรับตัวอย่างผลงานที่ผ่านมา
7. ใช้ [[scripts/Scripts]] สำหรับ Export ผลลัพธ์