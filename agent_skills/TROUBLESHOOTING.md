# Troubleshooting

> ปัญหาที่พบบ่อยและวิธีแก้ — สำหรับ AI และผู้ใช้

---

## 1. การถอดเสียง (Transcribe)

### Groq API Error 500 / 502
**สาเหตุ:** Groq API เซิร์ฟเวอร์ขัดข้องชั่วคราว หรือไฟล์เสียงมีปัญหา
**แก้ไข:** สคริปต์จะ retry อัตโนมัติ 3 ครั้ง (รอบละ 5 วิ) ถ้ายังไม่หาย ให้รันใหม่

### Groq API Error 401 (Unauthorized)
**สาเหตุ:** `GROQ_API_KEY` ใน `.env` ไม่ถูกต้องหรือหมดอายุ
**แก้ไข:** ตรวจสอบ `.env` ที่โปรเจกต์ root ว่ามี key ถูกต้องหรือไม่

### ffmpeg / ffprobe not found
**สาเหตุ:** ยังไม่ได้ติดตั้ง FFmpeg
**แก้ไข (Windows):** `winget install Gyan.FFmpeg`

### UnicodeEncodeError: 'charmap' codec can't encode
**สาเหตุ:** PowerShell / Terminal รองรับเฉพาะ cp1252 แต่ชื่อไฟล์มี Unicode
**แก้ไข:** ตั้ง `$env:PYTHONIOENCODING = "utf-8"` ก่อนรัน

---

## 2. การ Export Excel

### ModuleNotFoundError: No module named 'openpyxl'
**สาเหตุ:** ยังไม่ได้ติดตั้ง openpyxl
**แก้ไข:** `pip install openpyxl`

### Output ไม่มีคะแนน Viral
**สาเหตุ:** รันด้วย export_viral_cuts.py เวอร์ชันเก่า (ก่อนเพิ่มคอลัมน์คะแนน)
**แก้ไข:** แต่ละ cut dict ต้องมีฟิลด์ `"score": X.XX`

---

## 3. ไฟล์อ้างอิง

### Wiki link ใน Obsidian เปิดไม่ได้
**สาเหตุ:** ชื่อไฟล์ไม่ตรงกับ wikilink (Obsidian case-sensitive)
**แก้ไข:** ใช้ Pascal Case เท่านั้น: `[[../contents/Arena of Valor]]` ไม่ใช่ `[[../contents/arena of valor]]`

### SRT ภาษาไทยอ่านยาก (คำติดกัน, เว้นวรรคผิด)
**สาเหตุ:** ASR (Whisper) ถอดเสียงภาษาไทยได้ไม่ดีพอ
**แก้ไข:** ใช้สคริปต์ `replace()` แก้คำพบบ่อย: ทะนู→ธนู, มอเดอร์→เมอร์เดอร์

---

## 4. Pipeline

### Video file >25MB
**สาเหตุ:** ไฟล์ใหญ่เกินกว่าส่ง Groq API โดยตรง
**แก้ไข:** ใช้ FFmpeg auto-chunk 10 นาที (transcribe.py ทำ automaitic)

### Cut ต่ำกว่า 30 วินาที
**สาเหตุ:** จุดน่าสนใจสั้นเกินไป
**แก้ไข:** ตัดเท่าที่มี ไม่ต้องขยาย context (Minimum 30 วิ)
