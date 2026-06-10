# Scripts

> รวม Python scripts สำหรับช่วยในการทำงาน Viral Cut Pipeline

---

## `export_viral_cuts.py`

Export รายการ Viral Cut เป็นไฟล์ Excel (`.xlsx`)

### Dependencies
- `openpyxl`
  ```bash
  pip install openpyxl
  ```

### วิธีใช้

```python
from scripts.export_viral_cuts import export_viral_cuts_to_excel

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

export_viral_cuts_to_excel(cuts, output_path="viral_cuts.xlsx")
```

หรือรันตรง:
```bash
python scripts/export_viral_cuts.py
```

### Output
- ไฟล์ Excel `.xlsx` พร้อม:
  - หัวตารางสีน้ำเงินเข้ม ตัวอักษรสีขาว
  - Auto Filter
  - Column widths ปรับอัตโนมัติ
  - หัวคอลัมน์: #, ประเภท (Category), ชื่อคลิป, เวลาเริ่มต้น, เวลาสิ้นสุด, ชื่อไฟล์นำเข้า (.mp4), ความยาวคลิป (Duration)

---

> 💡 ดู Workflow หลักได้ที่ [[WorkFlows#Step-6-optional-export--ส่งมอบ]]
