# Scripts

> รวม Python scripts สำหรับช่วยในการทำงาน Viral Cut Pipeline

---

## `export_viral_cuts.py`

Export รายการ Viral Cut ไปยัง `outputs/` และ `references/`

### Dependencies
- `openpyxl`
  ```bash
  pip install openpyxl
  ```

### ฟังก์ชันหลัก

#### `export_all(cuts, date_str=None)`
Export ไปยัง `outputs/` และ `references/` พร้อมกัน:
```python
from scripts.export_viral_cuts import export_all

cuts = [
    {
        "category": "Chaos",
        "title": "โมเมนต์พี่กับน้องทะเลาะกันกลางไลฟ์!",
        "start_time": "01:23:15",
        "end_time": "01:27:20",
        "filename": "livestream-2026-06-10.mp4",
        "duration": "4 นาที 5 วินาที"
    }
]

export_all(cuts)  # ไม่ต้องระบุ date_str ใช้ UTC auto
```

#### `export_viral_cuts_to_excel(cuts, output_path)`
Export เฉพาะ Excel ไปยัง path ที่กำหนด

### รันตรง
```bash
python scripts/export_viral_cuts.py
```

### โครงสร้าง Output
```
outputs/
  viral-cut-2026-06-10.xlsx

references/
  2026-06-10/
    viral-cut-2026-06-10.xlsx
```

---

## `transcribe.py`

ถอดเสียงจาก `.mp4` ใน `raw/` เป็น `.srt` โดยใช้ Groq API (Whisper)

### Dependencies
- `groq`
- `ffmpeg` (ต้องติดตั้งในระบบ)
- `python-dotenv` (optional สำหรับ `.env`)
  ```bash
  pip install groq python-dotenv
  ```

### การตั้งค่า
1. คัดลอก `scripts/.env.example` เป็น `.env` ใน root
2. ใส่ `GROQ_API_KEY` ของคุณใน `.env`
3. วางไฟล์ `.mp4` ใน `raw/`

### วิธีใช้
```python
from scripts.transcribe import transcribe

srt_path = transcribe("raw/livestream-2026-06-10.mp4")
print(f"Saved: {srt_path}")
```

หรือรันตรง:
```bash
python scripts/transcribe.py
```

### Output
- `raw/livestream-2026-06-10.srt` — subtitle พร้อม timestamp

---

> 💡 ดู Workflow หลักได้ที่ [[WorkFlows#Step-2-วิเคราะห์เนื้อหาแบบช่วงเวลา]]
