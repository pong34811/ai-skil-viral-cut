# Viral Cut

ค้นหา วิเคราะห์ และคัดเลือกช่วงเวลาที่มีศักยภาพสูงจากไฟล์ไลฟ์สตรีม (.mp4) เพื่อนำไปตัดต่อเป็นคลิปสั้นและคลิปยาว

## โครงสร้าง vault

```
├── agent_skills/
│   ├── Skills.md          — ภาพรวม Skill, เกณฑ์วิเคราะห์ 6 ด้าน, Output Schema
│   ├── WorkFlows.md       — ขั้นตอนการทำงาน 6 Step
│   └── Rules.md           — ข้อจำกัด, หลักเกณฑ์, Quality Checklist
├── scripts/
│   ├── Scripts.md         — เอกสารการใช้งาน script
│   └── export_viral_cuts.py — Export Excel + SRT
├── raw/                   — วางไฟล์ .mp4 ที่นำเข้า
├── outputs/               — ไฟล์ผลลัพธ์ .xlsx
├── references/            — ข้อมูลอ้างอิงแบ่งตามวันที่
│   └── YYYY-MM-DD/
│       └── viral-cut-YYYY-MM-DD.xlsx
└── Welcome.md
```

## เริ่มต้น
1. วางไฟล์ `.mp4` ใน `raw/`
2. เปิด [[agent_skills/Skills]] เพื่อดูเกณฑ์การวิเคราะห์
3. ดู [[agent_skills/WorkFlows]] สำหรับขั้นตอน
4. ตรวจสอบ [[agent_skills/Rules]] สำหรับข้อควรระวัง
5. ใช้ [[scripts/Scripts]] สำหรับ Export ผลลัพธ์