# Plan: Viral Cut Pipeline

> คำสั่งแบบขั้นตอนสำหรับ AI อ่านและปฏิบัติตาม

---

## [ ] Step 0: อ่าน Skill ทั้งหมดก่อนเริ่ม

> ทุกครั้งที่ได้รับงานใหม่ ให้อ่านเอกสารทั้งหมดก่อนเริ่ม Step 1

- [ ] **Skills.md** — ทำความเข้าใจภาพรวม, Output Schema, วิธีเริ่ม
- [ ] **Rules.md** — ทำความเข้าใจข้อจำกัด, AI Behavior Rules
- [ ] **WorkFlows.md** — ทำความเข้าใจ workflow ทีละขั้นตอน
- [ ] **Viral-Cut-Detection.md** — ทำความเข้าใจเกณฑ์วิเคราะห์ 6 ด้าน + สูตร
- [ ] **Personas.md** — ทำความเข้าใจกลุ่มผู้ใช้งานเป้าหมาย
- [ ] **References.md** — ดูตัวอย่างผลงานก่อนหน้า เป็นแนวทาง
- [ ] **contents.md** — ตรวจสอบเกมที่มีข้อมูลอยู่แล้ว
- [ ] **plan.md** — ทำความเข้าใจ checklist ที่ต้องทำ
- [ ] **`.opencode/skills/viral-cut-detection/SKILL.md`** — ภาพรวม Skill

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

## [x] Step 2.5: ตรวจทานคำผิด

- [x] อ่าน `.srt` ทั้งหมด
- [x] แก้คำที่ transcribe ผิด:
  - [x] สะกดชื่อเกม, ตัวละคร, ชื่อคนให้ถูก
  - [x] แก้คำที่เสียงใกล้เคียงแต่ความหมายผิด
  - [x] ตรวจภาษาไทย: คำติดกัน, เว้นวรรคผิด
  - [x] ภาษาอังกฤษปน: แก้สเปลลิง
- [x] บันทึกทับไฟล์ `.srt` เดิม

## [ ] Step 2.6: สร้าง Reference MD (เฉพาะกรณี Reference Clip เท่านั้น)

> ใช้เมื่อทำงานกับไฟล์ `.srt` reference โดยตรง (ไม่มี `.mp4` ใน `raw/`)

- [ ] ตรวจสอบว่าเป็น Reference Clip หรือ Full Pipeline
- [ ] สร้าง `references/YYYY-MM-DD/{ชื่อคลิป}/{ชื่อคลิป}.md`:
  - [ ] ข้อมูลทั่วไป: ประเภท, ชื่อคลิป, เกม, ความยาว
  - [ ] เนื้อหา: สรุปสั้น ๆ ว่าคลิปเกี่ยวกับอะไร
  - [ ] จุดเด่น / Viral Potential: วิเคราะห์ตามเกณฑ์ 6 ด้าน
  - [ ] Reference: ลิงค์ไป References.md, contents.md, ไฟล์ SRT
- [ ] จัดเก็บ `.srt` ไว้ในโฟลเดอร์เดียวกับ `.md`
- [ ] อัปเดต `References.md` — เพิ่มรายการ reference clip ล่าสุด
- [ ] อัปเดต `Welcome.md` — เพิ่มสถานะ reference clip

## [ ] Step 3: วิเคราะห์เนื้อหา

- [ ] อ่าน `.json` หรือ `.srt` transcript
- [ ] ค้นหาช่วงที่เข้าข่าย Viral Cut ตามเกณฑ์:
  - [ ] Emotion Spike (20%)
  - [ ] Chaos / Conflict (20%)
  - [ ] Humor / Comedy Timing (20%)
  - [ ] Interaction Hook (15%)
  - [ ] Plot Twist / Unexpected (15%)
  - [ ] Educational / Insight (10%)
- [ ] แต่ละ cut ต้องมีความยาว **40 วินาที - 3 นาที** (ขั้นต่ำ 40 วินาที)
- [ ] ถ้าจุดน่าสนใจสั้นกว่า 40 วินาที → ขยายขอบเขตเก็บ context โดยรอบ

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

## [ ] Step 7: อัปเดตไฟล์ + ตรวจสอบ Consistency

### อัปเดตไฟล์
- [ ] **plan.md** — ติ๊ก `[x]` ทุก Step ที่ทำเสร็จแล้วทันที (อย่ารอเก็บทีเดียว)
- [ ] **agent_skills/References.md** — เพิ่มรายการ cuts ล่าสุด
- [ ] **agent_skills/contents.md** — ถ้ามีเกมใหม่ เพิ่มแถวในตารางลิงค์ไป `contents/{ชื่อเกม}`
- [ ] **agent_skills/chat-history.md** — บันทึก session log การแชท
- [ ] **agent_skills/Personas.md** — อัปเดตข้อมูล Persona ถ้ามีข้อมูลใหม่
- [ ] **Welcome.md** — อัปเดตสถานะโปรเจกต์

### ตรวจสอบ Consistency
- [ ] `contents/` directory — มีไฟล์ตรงกับตารางใน `contents.md` หรือไม่
- [ ] `contents.md` — มีแถวครบทุกเกมที่อยู่ใน `contents/` หรือไม่
- [ ] `References.md` — ลิงค์ไปยังไฟล์ที่มีอยู่จริงหรือไม่

## [ ] ข้อควรระวัง

- [ ] `.env` มี `GROQ_API_KEY` — ห้าม commit
- [ ] ห้าม commit/push โดยไม่ได้รับอนุญาตจากผู้ใช้
- [ ] ถ้า Error ตอน transcribe → ตรวจสอบ API key และ internet connection
- [ ] ไฟล์ใน `raw/` และ `outputs/` อยู่ใน `.gitignore` แล้ว
