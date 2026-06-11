# Viral Cut Detection Skill

AI Agent Skill for detecting viral moments from livestream `.mp4` files. Transcribes audio (Groq Whisper), scores segments on 6 viral criteria, ranks by weighted formula, and exports to Excel.

---

## ติดตั้ง Skill

### วิธีที่ 1: npx skills (แนะนำ)

```bash
npx skills add pong34811/ai-skil-viral-cut@viral-cut-detection -g -y
```

### วิธีที่ 2: วางไฟล์ตรง (Manual)

**สำหรับใช้เฉพาะโปรเจกต์นี้:**
```bash
copy ".opencode\skills\viral-cut-detection\SKILL.md" "%USERPROFILE%\.opencode\skills\viral-cut-detection\SKILL.md"
```

**สำหรับใช้ทุกโปรเจกต์ (Global):**
```bash
copy ".opencode\skills\viral-cut-detection\SKILL.md" "%USERPROFILE%\.config\opencode\skills\viral-cut-detection\SKILL.md"
```

### วิธีที่ 3: รัน .bat
- ดับเบิลคลิก `install_skill.bat` ที่ root โปรเจกต์

---

## วิธีใช้งาน

1. วางไฟล์ `.mp4` ใน `raw/`
2. ส่ง prompt ไปที่ AI:
   ```
   เริ่มงานตาม skill viral-cut-detection
   video_path: raw/<ชื่อไฟล์>.mp4
   title: "ชื่อไลฟ์"
   duration: HH:MM:SS
   ```
3. AI จะทำงานตาม WorkFlow 6 Steps:
   - รับไฟล์ + ตรวจสอบ
   - ถอดเสียง (Groq Whisper)
   - ให้คะแนน 6 เกณฑ์
   - คัดเลือก cut
   - สร้าง Output
   - Export Excel

---

## โครงสร้างโฟลเดอร์

```
├── agent_skills/            — เอกสารอ้างอิง (Skills, WorkFlows, Rules)
├── .opencode/skills/        — Skill definition สำหรับ opencode
├── scripts/
│   ├── transcribe.py        — ถอดเสียงด้วย Groq API
│   └── export_viral_cuts.py — Export ผลลัพธ์เป็น Excel
├── contents/                — ข้อมูลเกมสำหรับอ้างอิง
├── raw/                     — วางไฟล์ .mp4 ที่นำเข้า
├── outputs/                 — ไฟล์ผลลัพธ์ .xlsx
└── references/              — ข้อมูลอ้างอิงแบ่งตามวันที่
```

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
