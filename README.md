# Viral Cut Detection

AI Agent Skill สำหรับตรวจจับช่วงเวลาที่มีศักยภาพไวรัลจากไฟล์ไลฟ์สตรีม `.mp4` ถอดเสียงด้วย Groq Whisper, ให้คะแนน 6 เกณฑ์, คำนวณคะแนนถ่วงน้ำหนัก, และ Export เป็น Excel

---

## โครงสร้างโฟลเดอร์

```
├── agent_skills/              — เอกสารอ้างอิง (Skills, Rules, WorkFlows, plan)
│   ├── Skills.md              — ภาพรวม Skill, Output Schema
│   ├── Rules.md               — ข้อจำกัด, AI Behavior Rules
│   ├── WorkFlows.md           — ขั้นตอนการทำงาน
│   ├── Viral-Cut-Detection.md — เกณฑ์วิเคราะห์ 6 ด้าน + สูตร
│   ├── References.md          — ตัวอย่างผลงาน
│   ├── contents.md            — ตารางข้อมูลเกม
│   └── plan.md                — Checklist การทำงาน
├── .opencode/skills/          — Skill definition สำหรับ OpenCode
├── contents/                  — ข้อมูลเกมสำหรับอ้างอิง
├── scripts/
│   ├── transcribe.py          — ถอดเสียงด้วย Groq API
│   └── export_viral_cuts.py   — Export ผลลัพธ์เป็น Excel
├── raw/                       — วางไฟล์ .mp4 ที่นำเข้า
├── outputs/                   — ไฟล์ผลลัพธ์ .xlsx
├── references/                — ข้อมูลอ้างอิงแบ่งตามวันที่
│   └── YYYY-MM-DD/
│       ├── viral-cut-YYYY-MM-DD.xlsx
│       └── <ชื่อคลิป>/         — SRT + Reference MD
├── Welcome.md
├── example.txt                — Template สำหรับเริ่มงาน
└── README.md
```

---

## สำหรับผู้ใช้ OpenCode

เพิ่ม Skill ใน `.config/opencode/opencode.jsonc` แล้ว restart:

```json
{
  "plugin": ["superpowers@git+https://github.com/obra/superpowers.git"]
}
```

---

## วิธีใช้งาน

### Full Pipeline (มี .mp4 ใน raw/)

1. วางไฟล์ `.mp4` ใน `raw/`
2. ส่ง prompt:

```text
เริ่มงานตาม agent_skill
video_path: raw/<ไฟล์>.mp4
title: <ชื่อไลฟ์>
duration: HH:MM:SS
type: เกม หรือ Free talk
game: <ชื่อเกม> (ถ้า type=เกม)
metadata:
  date: YYYY-MM-DD
  platform: YouTube / Twitch / TikTok
```

3. AI จะทำงานตาม workflow:
   - **Step 0** — อ่าน Skill ทั้งหมดก่อนเริ่ม
   - **Step 1** — รับไฟล์ + metadata
   - **Step 2** — ถอดเสียง Groq Whisper (.srt + .json)
   - **Step 2.5** — ตรวจทานคำผิด
   - **Step 3** — วิเคราะห์เนื้อหา 6 เกณฑ์
   - **Step 4** — คัดเลือก + ให้คะแนนถ่วงน้ำหนัก
   - **Step 5** — Export Excel
   - **Step 6** — อัปเดต References.md  
   - **Step 7** — consistency check + อัปเดต Welcome.md

### Reference Clip (มี .srt ล้วน ไม่มี .mp4)

AI จะทำ Step 2.5 (spell-check) + Step 2.6 (สร้าง Reference MD)

---

## เกณฑ์การให้คะแนน

| เกณฑ์ | น้ำหนัก |
|-------|--------|
| Emotion Spike | 20% |
| Chaos / Conflict | 20% |
| Humor / Comedy Timing | 20% |
| Interaction Hook | 15% |
| Plot Twist / Unexpected | 15% |
| Educational / Insight | 10% |

**สูตร:** `(Emotion × 0.2) + (Chaos × 0.2) + (Humor × 0.2) + (Interaction × 0.15) + (PlotTwist × 0.15) + (Educational × 0.1)`

---

## ดูเพิ่มเติม

- `agent_skills/Skills.md` — ภาพรวม, Output Schema
- `agent_skills/Rules.md` — ข้อจำกัด, Quality Checklist
- `agent_skills/WorkFlows.md` — ขั้นตอนโดยละเอียด
- `agent_skills/plan.md` — Checklist ปฏิบัติการ
- `example.txt` — Template prompt สำหรับเริ่มงาน
