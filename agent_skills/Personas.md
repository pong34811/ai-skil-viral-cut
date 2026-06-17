# Personas

> ข้อมูลผู้ใช้งานเป้าหมายของโปรเจกต์นี้ — ใช้ร่วมกับ [[Skills]], [[WorkFlows]], [[Rules]] และ [[Viral-Cut-Detection]]

## Persona: Content Creator / Video Clip Selector (Viral Cut Pipeline)

### ข้อมูลทั่วไป

- **ชื่อ:** มินตรา
- **อายุ:** 24–32 ปี
- **อาชีพ:** คอนเทนต์ครีเอเตอร์ / เอดิตเตอร์ / ผู้ช่วยตัดต่อคลิป
- **เป้าหมายหลัก:** สร้างคอนเทนต์ที่น่าสนใจจากวิดีโอไลฟ์สตรีม (.mp4) โดยใช้ **Viral Cut Detection Pipeline** ([[Viral-Cut-Detection]]) เพื่อเลือกช่วงเวลาที่เด่นที่สุดไปตัดต่อคลิปสั้นลง YouTube Shorts / TikTok / Facebook Reels

---

### ลักษณะการทำงาน

มินตรารับชมไลฟ์สตรีม Vtuber / เกม ที่มีความยาว 1–7 ชั่วโมง (1280×720, 30fps, h264) เพื่อทำความเข้าใจเนื้อหา บรรยากาศ อารมณ์ และจังหวะ ปัจจุบันเธอใช้ pipeline 7 ขั้นตอนตาม [[WorkFlows]]:

1. **Step 0:** อ่าน [[Skills]] ทั้งหมดก่อนเริ่ม
2. **Step 1:** ตรวจสอบไฟล์ .mp4 → ขอ metadata → ตรวจ `contents/{game}.md` (ดู [[contents]])
3. **Step 2:** ถอดเสียงด้วย Groq Whisper (auto-chunk 10 นาที) → `.srt` + `.json` → ตรวจคำผิดใน SRT
4. **Step 3:** วิเคราะห์ 6 เกณฑ์ตาม [[Viral-Cut-Detection]] — Emotion / Chaos / Humor / Interaction / PlotTwist / Educational
5. **Step 4:** ให้คะแนนถ่วงน้ำหนักตามสูตรใน [[Viral-Cut-Detection#การประเมินศักยภาพไวรัล-viral-potential-scoring]]
6. **Step 5:** จัดลำดับตัด overlap → เลือก Top N cut (≥ 6.0 คะแนน, ≥ 40 วินาที ตาม [[Rules#2-ข้อจำกัดด้านระยะเวลา-duration-rules]])
7. **Step 6:** Export → `outputs/viral-cut-YYYY-MM-DD.xlsx` + `references/YYYY-MM-DD/`

คัดเลือกช่วงที่น่าสนใจ เช่น:

- ช่วง Chaos / Conflict — เหตุการณ์วุ่นวาย โกลาหล
- ช่วง Emotion Spike — อารมณ์พุ่งสูง โกรธ ตกใจ หัวเราะ
- ช่วง Humor / Comedy — จังหวะตลก, Meme-worthy moments
- ช่วง Interaction Hook — โต้ตอบผู้ชมหรือแขกรับเชิญ
- ช่วง Plot Twist — สิ่งที่ไม่คาดคิด พลิกผัน
- ช่วง Educational — ความรู้หรือข้อคิดที่แทรกอยู่

---

### สิ่งที่มินตราต้องการ

- pipeline ที่ถอดเสียง Groq Whisper ให้ SRT ถูกต้อง (โดยเฉพาะชื่อเกมภาษาไทย-อังกฤษปน)
- ระบบวิเคราะห์ 6 เกณฑ์ที่ตรงกับธรรมชาติของไลฟ์ Vtuber / เกม
- คะแนน Viral Score แบบถ่วงน้ำหนัก ช่วยจัดลำดับความสำคัญ
- Excel export ที่มี Category, Title, Start/End Time, Duration, Scores
- คู่มืออ้างอิงเกมใน `contents/{game}.md` (ดู [[contents]]) เพื่อใช้เป็นบริบทตอนวิเคราะห์
- ตัวอย่างผลงานก่อนหน้าใน [[References]] เพื่อเทียบเคียง

---

### ปัญหาที่พบบ่อย

- ไฟล์ .mp4 มีขนาดใหญ่ (>1GB) ต้อง auto-chunk 10 นาทีผ่าน FFmpeg
- Groq API error (500, 401, 502) โดยเฉพาะ chunk ท้าย ๆ → ต้อง retry
- คำศัพท์เฉพาะเกม / Vtuber อ่านผิด: "Cheese Rolling" → "Cheat Rolling" ต้องตรวจ SRT
- ระยะเวลาตัดสินใจ cut ที่ overlap กัน → ต้อง merge หรือเลือกคะแนนสูงสุด
- SRT บรรทัดภาษาไทยมักติดกันหรือเว้นวรรคผิด ต้อง proofread

---

### แรงจูงใจ

- ต้องการลดเวลาจากการดูคลิปยาว 98 นาทีเหลือแค่อ่าน SRT + JSON ที่ถอดเสียงแล้ว
- ต้องการเพิ่มโอกาสให้คลิปสั้นกลายเป็นไวรัล โดยใช้คะแนนจาก 6 เกณฑ์
- ต้องการระบบที่จัดการ chunk + retry ให้อัตโนมัติ
- ต้องการ output .xlsx ที่พร้อมส่งต่อให้ทีมตัดต่อ

---

### พฤติกรรมการใช้งาน AI

มินตราใช้ AI เป็นผู้ช่วยเต็มรูปแบบใน pipeline:

- ถอดเสียง Groq Whisper → `.srt` + `.json`
- ตรวจคำผิดใน SRT (ชื่อเกม, ชื่อ Vtuber, คำภาษาไทย-อังกฤษ)
- วิเคราะห์ transcript ตาม 6 เกณฑ์ → ให้คะแนน weighted score
- เลือก Top N cut ที่ ≥ 6.0 คะแนน, ≥ 40 วินาที, ไม่ overlap
- Export Excel → `outputs/viral-cut-YYYY-MM-DD.xlsx`
- สร้างไฟล์อ้างอิง → `references/YYYY-MM-DD/`
- ตั้งชื่อคลิปและเขียนคำอธิบาย
- อัปเดต `References.md`, `contents.md`, `chat-history.md`, `Welcome.md`

AI ช่วยให้มินตราลดเวลาทำงานจากหลายชั่วโมงเหลือเพียง pipeline เดียว ตั้งแต่ raw .mp4 → Excel ที่พร้อมใช้งาน
