# chat-history.md — Design Spec

## Purpose
บันทึก full log ของทุกข้อความที่แชทกับ AI ไว้ในไฟล์เดียว เพื่อให้สามารถย้อนดูประวัติการสนทนาได้

## Location
`agent_skills/chat-history.md`

## Format
- Chronological เรียงตามวัน session
- หัวข้อวันที่เป็น `## YYYY-MM-DD`
- ข้อความแยกเป็น `**User:**` และ `**AI:**`
- วันล่าสุดอยู่ล่างสุด (append ต่อท้าย)

## Example Structure
```markdown
# Chat History

## 2026-06-10

**User:** example message
**AI:** example response

## 2026-06-11

**User:** another message
**AI:** another response
```

## Implementation
- สร้างไฟล์เปล่าพร้อมหัวข้อ `# Chat History`
- ไม่ต้อง commit ทันที
