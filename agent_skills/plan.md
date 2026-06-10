# Plan: Viral Cut Pipeline

> คำสั่งแบบขั้นตอนสำหรับ AI อ่านและปฏิบัติตาม

---

## [ ] Step 1: รับไฟล์

- [ ] รับ path ไฟล์ `.mp4` จากผู้ใช้
- [ ] ตรวจสอบว่าไฟล์อยู่ใน `raw/`
- [ ] ถ้า title / metadata ไม่มี ให้ถามผู้ใช้:
  - [ ] **title** — ชื่อไลฟ์
  - [ ] **metadata** — วันที่, แพลตฟอร์ม, ผู้ร่วม stream (ถ้ามี)
- [ ] ถามประเภทเนื้อหา:
  - [ ] ถ้าเป็น **เกม**: ถามชื่อเกม → ตรวจ `contents/{ชื่อเกม}.md`
    - [ ] มีอยู่แล้ว: อ่านเป็นข้อมูลประกอบ
    - [ ] ไม่มี: ค้นหาเว็บ → สร้าง `contents/{ชื่อเกม}.md` → อัปเดต `agent_skills/contents.md`
  - [ ] ถ้าเป็น **Free talk**: ไม่ต้องหาเกม
- [ ] ดึงข้อมูลไฟล์: duration, resolution, FPS, file size
- [ ] ตรวจสอบความสมบูรณ์ของไฟล์ (ffprobe)

## [ ] Step 2: ถอดเสียง

- [ ] รัน `python scripts/transcribe.py "raw/<file>.mp4" --srt --json`
  - [ ] `--srt` → `.srt` subtitle
  - [ ] `--json` → `.json` segments + words
  - [ ] ไฟล์ >25MB auto-chunk 10 นาที
- [ ] ถ้า Error: check `scripts/.env` ว่ามี `GROQ_API_KEY` หรือไม่

## [ ] Step 3: วิเคราะห์เนื้อหา

- [ ] อ่าน `.json` หรือ `.srt` transcript
- [ ] ค้นหาช่วงที่เข้าข่าย Viral Cut ตามเกณฑ์:
  - [ ] Emotion Spike (20%)
  - [ ] Chaos / Conflict (20%)
  - [ ] Humor / Comedy Timing (20%)
  - [ ] Interaction Hook (15%)
  - [ ] Plot Twist / Unexpected (15%)
  - [ ] Educational / Insight (10%)
- [ ] แต่ละ cut ต้องมีความยาว **1-3 นาที** เท่านั้น (ห้ามต่ำกว่า 1 นาที)
- [ ] ถ้าจุดน่าสนใจสั้นกว่า 1 นาที → ขยายขอบเขตเก็บ context โดยรอบ

## [ ] Step 4: คัดเลือกและให้คะแนน

- [ ] คำนวณคะแนนรวม: `(Emotion×0.2)+(Chaos×0.2)+(Humor×0.2)+(Interaction×0.15)+(PlotTwist×0.15)+(Educational×0.1)`
- [ ] เรียงลำดับตามคะแนนจากมากไปน้อย
- [ ] เลือก Top N cuts (แนะนำ 4-8 cut สำหรับวิดีโอ 1-2 ชม.)
- [ ] ตัดสินใจ Tie-breaker: Chaos → Humor → Interaction
- [ ] ตรวจสอบว่าไม่มี timeline ซ้อนทับกัน
- [ ] ตรวจสอบว่าแต่ละ cut กระจายตัวไม่กระจุก

## [ ] Step 5: Export

- [ ] เขียน cuts ตาม schema:
```
{
    "category": "...",
    "title": "...",
    "start_time": "HH:MM:SS",
    "end_time": "HH:MM:SS",
    "filename": "<file>.mp4",
    "duration": "X นาที X วินาที"
}
```
- [ ] รัน export:
```python
from scripts.export_viral_cuts import export_all
export_all(cuts)
```
- [ ] เช็ค `outputs/viral-cut-YYYY-MM-DD.xlsx` — ผลลัพธ์หลัก
- [ ] เช็ค `references/YYYY-MM-DD/viral-cut-YYYY-MM-DD.xlsx` — อ้างอิง

## [ ] Step 6: อัปเดตไฟล์

- [ ] **agent_skills/References.md** — เพิ่มรายการ cuts ล่าสุด
- [ ] **Welcome.md** — อัปเดตสถานะโปรเจกต์
- [ ] **contents/{game}.md** — ถ้ามีข้อมูลเกมใหม่ เพิ่ม/อัปเดต

## [ ] ข้อควรระวัง

- [ ] `.env` มี `GROQ_API_KEY` — ห้าม commit
- [ ] ห้าม commit/push โดยไม่ได้รับอนุญาตจากผู้ใช้
- [ ] ถ้า Error ตอน transcribe → ตรวจสอบ API key และ internet connection
- [ ] ไฟล์ใน `raw/` และ `outputs/` อยู่ใน `.gitignore` แล้ว
