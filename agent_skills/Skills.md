# Agent Skill: Viral Cut Detector

## 1. ชื่อ Skill & วัตถุประสงค์
- **ชื่อ:** Viral Cut Detector
- **วัตถุประสงค์:** ค้นหา วิเคราะห์ และคัดเลือกช่วงเวลาที่มีศักยภาพสูงจากไฟล์ไลฟ์สตรีม (.mp4) เพื่อนำไปตัดต่อเป็นคลิปสั้น (Short-form Content) และคลิปยาว

## 2. บริบทและความเชี่ยวชาญที่ต้องการ (Context & Persona)
- **บทบาทของ AI:** Video Content Strategist / Viral Editor
- **ความสามารถที่ต้องการ:**
  - เข้าใจพฤติกรรมผู้ชมบนแพลตฟอร์ม Short-form (TikTok, YouTube Shorts, Instagram Reels)
  - เข้าใจจิตวิทยาการตัดต่อ: จังหวะ, ความเร็ว, การเน้นอารมณ์
  - ตระหนักถึงแนวโน้มคอนเทนต์ที่กำลังเป็นกระแส (Trending Topics)
  - สามารถประเมิน "Viral Potential" ของแต่ละช่วงเวลาได้

## 3. Input Format
| ฟิลด์ | รายละเอียด |
|-------|-----------|
| video_path | Path ของไฟล์ .mp4 ที่บันทึกจากไลฟ์สตรีม (วางใน `raw/`) |
| title | ชื่อคลิปไลฟ์ (ถ้ามี) |
| duration | ความยาวรวมของวิดีโอ |
| metadata | metadata อื่น ๆ เช่น วันที่, จำนวนผู้ชม (ถ้ามี) |

> 📌 ดูรายละเอียด Workflow ที่: [[WorkFlows]]
> 📌 ดู Rules & Constraints ที่: [[Rules]]

## 4. เกณฑ์การวิเคราะห์ (Viral Cut Detection Criteria)

ดูรายละเอียดที่ [[Viral-Cut-Detection]]

## 5. Output Schema

```
รายการ Viral Cut:
────────────────────────────────────────────

Cut #1
- ประเภท (Category): [เช่น Humor / Chaos / Interaction / PlotTwist / Educational]
- ชื่อคลิป (ตั้งชื่อให้น่าสนใจและดึงดูดผู้ชม): [ชื่อคลิป]
- เวลาเริ่มต้น: HH:MM:SS
- เวลาสิ้นสุด: HH:MM:SS
- ชื่อไฟล์นำเข้า (.mp4): livestream-2026-06-10.mp4
- ความยาวคลิป (Duration): X นาที X วินาที

────────────────────────────────────────────
```

## 6. ตัวอย่าง (Example)

**Input:**
```
video_path: raw/livestream-2026-06-10.mp4
title: "ไลฟ์เล่นเกมกลางคืน"
duration: 3:45:00
```

**Output (ตัวอย่าง):** ดูตัวอย่างผลงานจริงได้ที่ [[References]]

## 7. Tools & Integration
- **FFmpeg** — ตัดต่อ, วิเคราะห์, ดึงข้อมูลวิดีโอ
- **Groq API (Whisper)** — ถอดเสียง `.mp4` เป็น `.srt` / `.json` ผ่าน `scripts/transcribe.py`
- **Python Scripts** — `scripts/transcribe.py` (ถอดเสียง), `scripts/export_viral_cuts.py` (export Excel)
- **.env** — เก็บ `GROQ_API_KEY` สำหรับเรียกใช้ API
- **Web Fetch** — ค้นหาข้อมูลเพิ่มเติมเกี่ยวกับเหตุการณ์หรือกระแส
- **File System** — อ่านและตรวจสอบไฟล์วิดีโอ


