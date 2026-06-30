# AGENTS.md — Auto-update Obsidian after every task

After every task completion (transcribe, analyze, export, edit, create, delete, rename, etc.):
→ Automatically update ALL Obsidian vault files listed below. Do NOT wait for the user to ask.

## Files to update (หลังทำงานเสร็จทุกครั้ง)

| # | ไฟล์ | การอัปเดต |
|---|------|-----------|
| 1 | `Welcome.md` | เพิ่ม/อัปเดต section สถานะล่าสุดของโปรเจกต์ |
| 2 | `agent_skills/References.md` | เพิ่ม reference entries ใหม่ ถ้ามี cuts/clips ใหม่ |
| 3 | `agent_skills/contents.md` | เพิ่มแถวเกมใหม่ในตาราง ถ้าสร้าง `contents/<game>.md` ใหม่ |
| 4 | `agent_skills/plan.md` | ติ๊ก `[x]` steps ที่ทำเสร็จแล้ว |
| 5 | `agent_skills/Personas.md` | อัปเดตข้อมูล Persona ถ้ามีข้อมูลใหม่ |

## Consistency checks (หลังอัปเดตเสร็จ)

- [ ] `contents/` directory กับ `agent_skills/contents.md` — ตรงกัน
- [ ] ลิงค์ใน `agent_skills/References.md` — ชี้ไปไฟล์ที่มีอยู่จริง
- [ ] ไฟล์ใหม่ (.md) ทุกไฟล์มี wiki link เชื่อมโยงใน Welcome.md หรือ index files
- [ ] timestamp format: `HH:MM:SS` เท่านั้น
- [ ] output filenames ใช้ UTC date (`YYYY-MM-DD`)
