import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime
import os

def export_viral_cuts_to_excel(cuts, output_path="viral_cuts.xlsx"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Viral Cuts"

    header_font = Font(name="Arial", bold=True, color="FFFFFF", size=11)
    header_fill = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
    header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin_border = Border(
        left=Side(style="thin"), right=Side(style="thin"),
        top=Side(style="thin"), bottom=Side(style="thin"),
    )

    headers = [
        "#", "ประเภท (Category)", "ชื่อคลิป", "เวลาเริ่มต้น", "เวลาสิ้นสุด",
        "ชื่อไฟล์นำเข้า (.mp4)", "ความยาวคลิป (Duration)"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = thin_border

    data_font = Font(name="Arial", size=10)
    data_align = Alignment(vertical="center", wrap_text=True)

    for row_idx, cut in enumerate(cuts, 2):
        values = [
            row_idx - 1,
            cut.get("category", ""),
            cut.get("title", ""),
            cut.get("start_time", ""),
            cut.get("end_time", ""),
            cut.get("filename", ""),
            cut.get("duration", ""),
        ]
        for col, value in enumerate(values, 1):
            cell = ws.cell(row=row_idx, column=col, value=value)
            cell.font = data_font
            cell.alignment = data_align
            cell.border = thin_border

    col_widths = [5, 22, 40, 14, 14, 30, 22]
    for i, width in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width

    ws.row_dimensions[1].height = 30
    for row in range(2, len(cuts) + 2):
        ws.row_dimensions[row].height = 40

    ws.auto_filter.ref = f"A1:G{len(cuts) + 1}"

    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    wb.save(output_path)
    return output_path


def export_all(cuts, date_str=None):
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")

    filename = f"viral-cut-{date_str}"

    out = export_viral_cuts_to_excel(cuts, output_path=f"outputs/{filename}.xlsx")
    print(f"Output: {out}")

    ref = export_viral_cuts_to_excel(cuts, output_path=f"references/{date_str}/{filename}.xlsx")
    print(f"Reference: {ref}")


if __name__ == "__main__":
    example_cuts = [
        {
            "category": "Chaos",
            "title": "โมเมนต์พี่กับน้องทะเลาะกันกลางไลฟ์!",
            "start_time": "01:23:15",
            "end_time": "01:27:20",
            "filename": "livestream-2026-06-10.mp4",
            "duration": "4 นาที 5 วินาที"
        },
        {
            "category": "Interaction",
            "title": "แฟนคลับดอนเนท! 10,000 บาทแรกของไลฟ์",
            "start_time": "02:45:10",
            "end_time": "02:48:30",
            "filename": "livestream-2026-06-10.mp4",
            "duration": "3 นาที 20 วินาที"
        }
    ]
    export_all(example_cuts, date_str="2026-06-10")
