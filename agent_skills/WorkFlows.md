# Workflow: Viral Cut Detection Pipeline

> ไฟล์นี้เป็นส่วนหนึ่งของ [[skill]] — ดูเพิ่มเติมที่ [[Rules]]

---

## Step 1: รับและตรวจสอบไฟล์นำเข้า

1. ตรวจสอบว่าไฟล์ `.mp4` มีอยู่จริงและสามารถอ่านได้
2. ถ้ามี `youtube_url` ให้ดึง metadata เพิ่มเติมผ่าน YouTube API
3. ดึงข้อมูลพื้นฐานของวิดีโอ:
   - ความยาวรวม (duration)
   - Resolution
   - FPS (frames per second)
   - File size
4. ตรวจสอบความสมบูรณ์ของไฟล์ (corrupted หรือไม่)

## Step 2: วิเคราะห์เนื้อหาแบบช่วงเวลา

1. แบ่งวิดีโอเป็นช่วงย่อย (segment) ตามความยาวที่เหมาะสม:
   - สำหรับคลิปสั้น: segment ละ 30-60 วินาที
   - สำหรับคลิปยาว: segment ละ 1-3 นาที
2. วิเคราะห์แต่ละ segment ตามเกณฑ์ใน [[skill#4-เกณฑ์การวิเคราะห์-viral-cut-detection-criteria]]
3. บันทึกคะแนนแต่ละด้านพร้อมหมายเหตุ

## Step 3: ประเมินศักยภาพไวรัล (Viral Potential Scoring)

1. ให้คะแนนแต่ละ segment ในแต่ละเกณฑ์ (1-10)
2. คำนวณคะแนนรวมแบบถ่วงน้ำหนัก:

| เกณฑ์ | น้ำหนัก |
|-------|--------|
| Emotion Spike | 20% |
| Chaos / Conflict | 20% |
| Humor / Comedy Timing | 20% |
| Interaction Hook | 15% |
| Plot Twist / Unexpected | 15% |
| Educational / Insight | 10% |

3. **คะแนนรวม =** (Emotion × 0.2) + (Chaos × 0.2) + (Humor × 0.2) + (Interaction × 0.15) + (PlotTwist × 0.15) + (Educational × 0.1)

## Step 4: คัดเลือกและจัดลำดับ Viral Cut

1. เรียงลำดับ segment ตาม Viral Score จากมากไปน้อย
2. เลือก segment ที่มีคะแนนสูงสุด (Top N)
3. **ตรวจสอบความไม่ซ้ำซ้อน (overlap):**
   - ถ้า segment A และ B ทับซ้อนกัน ให้เลือกเฉพาะ segment ที่คะแนนสูงกว่า
   - ปรับ Timeline ให้ไม่ซ้อนทับ
4. จำแนกแต่ละ cut ตามประเภทเนื้อหาที่เด่นที่สุด
5. กำหนดชื่อคลิปที่น่าสนใจสำหรับแต่ละ cut

## Step 5: สร้าง Output ตาม Schema

1. สร้างรายการ Viral Cut ตามรูปแบบใน [[skill#5-output-schema]]
2. สำหรับแต่ละ cut:
   - Category
   - ชื่อคลิป
   - เวลาเริ่มต้นและสิ้นสุด (HH:MM)
   - ลิงก์ YouTube พร้อม Timestamp (หน่วยวินาที)
   - ความยาวคลิป
   - Viral Score
   - เหตุผลโดยย่อ
3. ตรวจสอบความถูกต้องผ่าน Quality Checklist ใน [[Rules]]

## Step 6: (Optional) Export & ส่งมอบ

1. (Optional) Export รายการเป็น JSON / CSV สำหรับการตัดต่ออัตโนมัติ
2. (Optional) สร้างไฟล์ EDL (Edit Decision List) สำหรับโปรแกรมตัดต่อ
3. ส่งมอบรายการให้ผู้ใช้
