# Workflow: Viral Cut Detection Pipeline

> ไฟล์นี้เป็นส่วนหนึ่งของ [[Skills]] — ดูเพิ่มเติมที่ [[Rules]]

---

## Step 1: รับและตรวจสอบไฟล์นำเข้า

1. รับไฟล์ `.mp4` จากผู้ใช้ วางไว้ในโฟลเดอร์ `raw/`
2. ตรวจสอบว่าไฟล์ใน `raw/` มีอยู่จริงและสามารถอ่านได้
3. ดึงข้อมูลพื้นฐานของวิดีโอ:
   - ความยาวรวม (duration)
   - Resolution
   - FPS (frames per second)
   - File size
4. ตรวจสอบความสมบูรณ์ของไฟล์ (corrupted หรือไม่)

## Step 2: ถอดเสียงและวิเคราะห์เนื้อหา

1. **ถอดเสียงด้วย Groq API** — ใช้ `scripts/transcribe.py` ถอดเสียง `.mp4` ใน `raw/` เป็น `.srt`
   ```python
   from scripts.transcribe import transcribe
   srt_path = transcribe("raw/livestream-2026-06-10.mp4")
   ```
2. **วิเคราะห์ transcript** — ใช้ `.srt` ที่ได้ค้นหาช่วงเวลาที่น่าสนใจ:
   - เหตุการณ์วุ่นวาย, จังหวะตลก, การโต้ตอบที่น่าสนใจ
   - จุดที่มีอารมณ์พุ่งสูงหรือเหตุการณ์สำคัญที่น่าจดจำ
3. คัดเลือกช่วงที่น่าสนใจ โดยมีความยาวประมาณ **1-3 นาที** ต่อ cut
4. วิเคราะห์แต่ละช่วงตามเกณฑ์ใน [[Skills#4-เกณฑ์การวิเคราะห์-viral-cut-detection-criteria]]
5. บันทึกคะแนนแต่ละด้านพร้อมหมายเหตุ

## Step 3: ประเมินศักยภาพไวรัล (Viral Potential Scoring)

1. ให้คะแนนแต่ละ segment ในแต่ละเกณฑ์ (1-10)
2. คำนวณคะแนนรวมแบบถ่วงน้ำหนัก โดยอ้างอิงจากหลายแหล่ง:

| เกณฑ์ | น้ำหนัก | อ้างอิง |
|-------|--------|--------|
| Emotion Spike | 20% | OpusClip (Hook/Flow/Value/Trend — emotional resonance factor), Munch AI (emotional peaks), Transcriptr (multi-signal fusion) |
| Chaos / Conflict | 20% | Archive Virality Score (engagement velocity signal), Eyko AI (identity signal, story arc) |
| Humor / Comedy Timing | 20% | Transcriptr (NLP speech pattern analysis), Higgsfield AI (hook retention window) |
| Interaction Hook | 15% | OpusClip (Hook strength factor), Quso AI (hook strength, narrative arc) |
| Plot Twist / Unexpected | 15% | Eyko AI (novelty detection, share-prompted format), Transcriptr (story arc detection) |
| Educational / Insight | 10% | OpusClip (Value factor — emotional & educational resonance), Quso AI (viewer value) |

3. **คะแนนรวม =** (Emotion × 0.2) + (Chaos × 0.2) + (Humor × 0.2) + (Interaction × 0.15) + (PlotTwist × 0.15) + (Educational × 0.1)

### ข้อมูลอ้างอิงหลัก (Sources)

| Source | รายละเอียด | ปี |
|--------|-----------|----|
| **OpusClip Virality Score** | วิเคราะห์ Hook, Flow, Value, Trend เพื่อให้คะแนน 0-99 ต่อ clip ([help.opus.pro](https://help.opus.pro/docs/article/virality-score)) | 2026 |
| **Munch AI** | ใช้ trending keywords, emotional peaks, speech patterns ในการวัดศักยภาพ ([getmunch.com](https://www.getmunch.com/)) | 2025 |
| **Archive Virality Score** | วัด view velocity + total views, แบ่งเป็น 4 tiers (High/Medium/Low/Not Viral) ([help.archive.com](https://help.archive.com/en/articles/14456753-understanding-archive-s-virality-score-metrics-updates)) | 2026 |
| **Transcriptr — Multi-Signal Fusion** | รวมคะแนนจาก NLP + Audio + Visual + Engagement ด้วย weighted model ([transcriptr.ai](https://transcriptr.ai/blog/ai-viral-moment-detection)) | 2026 |
| **Eyko AI — Viral Potential Scoring** | วัด emotional resonance, novelty, identity signal, story arc, share-prompted format ([eyko.ai](https://eyko.ai/ideas/viral-potential-scoring/)) | 2026 |
| **Quso AI (Vidyo AI)** | วัด hook strength, narrative arc, viewer value, trend alignment ([filmora.wondershare.com](https://filmora.wondershare.com/video-editor-review/quso-ai-review.html)) | 2026 |
| **Higgsfield AI — Engagement Score** | วัด retention time และ hook effectiveness ใน 3 วินาทีแรก ([higgsfield.ai](https://higgsfield.ai/apps/virality-predictor)) | 2026 |
| **YouTube Content Analyzer (Research Paper)** | ใช้ Random Forest + SMOTE + TF-IDF ทำนาย virality ด้วยความแม่นยำ 75% ([ResearchGate](https://www.researchgate.net/publication/401760676)) | 2026 |

> ⚠️ **หมายเหตุ:** น้ำหนักข้างต้นเป็นค่าประมาณเริ่มต้นที่ปรับจากหลายแหล่งข้างต้น สามารถปรับเปลี่ยนได้ตามข้อมูลเชิงลึกใหม่ ๆ ควรตรวจสอบและอัปเดตสูตรเป็นระยะ

## Step 4: คัดเลือกและจัดลำดับ Viral Cut

1. เรียงลำดับ segment ตาม Viral Score จากมากไปน้อย
2. เลือก segment ที่มีคะแนนสูงสุด (Top N)
3. **ตรวจสอบความไม่ซ้ำซ้อน (overlap):**
   - ถ้า segment A และ B ทับซ้อนกัน ให้เลือกเฉพาะ segment ที่คะแนนสูงกว่า
   - ปรับ Timeline ให้ไม่ซ้อนทับ
4. จำแนกแต่ละ cut ตามประเภทเนื้อหาที่เด่นที่สุด
5. กำหนดชื่อคลิปที่น่าสนใจสำหรับแต่ละ cut

## Step 5: สร้าง Output ตาม Schema

1. สร้างรายการ Viral Cut ตามรูปแบบใน [[Skills#5-output-schema]]
2. สำหรับแต่ละ cut:
   - ประเภท (Category)
   - ชื่อคลิป (ตั้งชื่อให้น่าสนใจและดึงดูดผู้ชม)
   - เวลาเริ่มต้น (HH:MM:SS)
   - เวลาสิ้นสุด (HH:MM:SS)
   - ชื่อไฟล์นำเข้า (.mp4)
   - ความยาวคลิป (Duration)
3. ตรวจสอบความถูกต้องผ่าน Quality Checklist ใน [[Rules]]

## Step 6: Export & ส่งมอบ

1. **Export หลัก** — ใช้ `scripts/export_viral_cuts.py`:
   ```python
   from scripts.export_viral_cuts import export_all
   export_all(cuts)  # auto ใช้วันที่ UTC ปัจจุบัน
   ```
   - `outputs/viral-cut-YYYY-MM-DD.xlsx` — ไฟล์ผลลัพธ์หลัก
   - `references/YYYY-MM-DD/viral-cut-YYYY-MM-DD.xlsx` — ไฟล์อ้างอิง

2. โครงสร้างไฟล์หลัง export:
   ```
   outputs/
     viral-cut-2026-06-10.xlsx
   references/
     2026-06-10/
       viral-cut-2026-06-10.xlsx
   ```

3. (Optional) Export เพิ่มเติมเป็น JSON / CSV / EDL สำหรับการตัดต่อ

4. ส่งมอบรายการให้ผู้ใช้

> ดูรายละเอียดเพิ่มเติมที่ [[../scripts/Scripts]]
