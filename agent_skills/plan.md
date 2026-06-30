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

## [x] Step 1: รับไฟล์

- [x] รับ path ไฟล์ `.mp4` จากผู้ใช้
- [x] ตรวจสอบว่าไฟล์อยู่ใน `raw/`
- [x] title / metadata: title="【🔴 LIVE】Minecraft   _ 27_04_2026 _ #katy404live", game=Minecraft, type=เกม
- [x] ถามประเภทเนื้อหา:
  - [x] ถ้าเป็น **เกม**: Minecraft → ตรวจ `contents/Minecraft.md`
    - [x] ไม่มี: ค้นหาเว็บ → สร้าง `contents/Minecraft.md` → อัปเดต `agent_skills/contents.md`
- [x] ดึงข้อมูลไฟล์: 1280×720, 30fps, h264, 1:23:33, 1.16 GB
- [x] ตรวจสอบความสมบูรณ์ของไฟล์ (ffprobe) ✅

## [x] Step 2: ถอดเสียง

- [x] รัน `python scripts/transcribe.py "raw/<file>.mp4" --srt --json`
  - [x] `--srt` → `.srt` subtitle
  - [x] `--json` → `.json` segments + words
  - [x] ไฟล์ >25MB auto-chunk 10 นาที
- [x] ถ้า Error: check `.env` (project root) ว่ามี `GROQ_API_KEY` หรือไม่

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

## [x] Step 3: วิเคราะห์เนื้อหา

- [x] อ่าน `.json` หรือ `.srt` transcript
- [x] ค้นหาช่วงที่เข้าข่าย Viral Cut ตามเกณฑ์:
  - [x] Emotion Spike (20%)
  - [x] Chaos / Conflict (20%)
  - [x] Humor / Comedy Timing (20%)
  - [x] Interaction Hook (15%)
  - [x] Plot Twist / Unexpected (15%)
  - [x] Educational / Insight (10%)
- [x] แต่ละ cut ต้องมีความยาว **30 วินาที - 3 นาที** (ขั้นต่ำ 30 วินาที)
- [x] ถ้าจุดน่าสนใจสั้นกว่า 30 วินาที → ตัดเท่าที่มี ไม่ต้องขยาย context

## [x] Step 4: คัดเลือกและให้คะแนน

- [x] คำนวณคะแนนรวม: `(Emotion×0.2)+(Chaos×0.2)+(Humor×0.2)+(Interaction×0.15)+(PlotTwist×0.15)+(Educational×0.1)`
- [x] เรียงลำดับตามคะแนนจากมากไปน้อย
- [x] เลือก Top N cuts (แนะนำ 4-8 cut สำหรับวิดีโอ 1-2 ชม.)
- [x] ตัดสินใจ Tie-breaker: Chaos → Humor → Interaction
- [x] ตรวจสอบว่าไม่มี timeline ซ้อนทับกัน
- [x] ตรวจสอบว่าแต่ละ cut กระจายตัวไม่กระจุก

## [x] Step 5: Export

- [x] เขียน cuts ตาม schema:
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
- [x] เช็ค `outputs/YYYY-MM-DD/viral-cut-YYYY-MM-DD.xlsx` — ผลลัพธ์หลัก
- [x] เช็ค `references/YYYY-MM-DD/viral-cut-YYYY-MM-DD.xlsx` — อ้างอิง

## [x] Step 6: ตัดคลิปวิดีโอ

> ใช้ `scripts/cut_clips.py` เพื่อตัดไฟล์ .mp4 ตาม timestamp จาก Excel

- [x] รัน `python scripts/cut_clips.py "raw/<file>.mp4" --cuts "outputs/viral-cut-2026-06-30.xlsx"`

## [x] Step 7: อัปเดตไฟล์ + ตรวจสอบ Consistency

### อัปเดตไฟล์
- [x] **plan.md** — ติ๊ก `[x]` ทุก Step ที่ทำเสร็จแล้วทันที (อย่ารอเก็บทีเดียว)
- [x] **agent_skills/References.md** — เพิ่มรายการ cuts ล่าสุด
- [x] **agent_skills/contents.md** — ถ้ามีเกมใหม่ เพิ่มแถวในตารางลิงค์ไป `contents/{ชื่อเกม}`
- [ ] **agent_skills/Personas.md** — อัปเดตข้อมูล Persona ถ้ามีข้อมูลใหม่
- [x] **Welcome.md** — อัปเดตสถานะโปรเจกต์

### ตรวจสอบ Consistency
- [x] `contents/` directory — มีไฟล์ตรงกับตารางใน `contents.md` หรือไม่
- [x] `contents.md` — มีแถวครบทุกเกมที่อยู่ใน `contents/` หรือไม่
- [x] `References.md` — ลิงค์ไปยังไฟล์ที่มีอยู่จริงหรือไม่

## [x] ข้อควรระวัง

- [x] `.env` มี `GROQ_API_KEY` — ห้าม commit
- [x] ห้าม commit/push โดยไม่ได้รับอนุญาตจากผู้ใช้
- [x] ถ้า Error ตอน transcribe → ตรวจสอบ API key และ internet connection
- [x] ไฟล์ใน `raw/`, `outputs/`, `references/` อยู่ใน `.gitignore` แล้ว
