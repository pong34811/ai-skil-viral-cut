import subprocess, os, sys, json, argparse
from datetime import datetime, timezone

def parse_time(t):
    parts = t.split(":")
    return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])

def find_ffmpeg():
    candidates = [
        "ffmpeg",
        r"C:\Users\warit\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe",
    ]
    for c in candidates:
        try:
            subprocess.run([c, "-version"], capture_output=True, check=False)
            return c
        except FileNotFoundError:
            continue
    return "ffmpeg"

def cut_clip(video_path, start, end, output_path, ffmpeg_path="ffmpeg"):
    duration = parse_time(end) - parse_time(start)
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    cmd = [
        ffmpeg_path, "-y", "-ss", start, "-i", video_path,
        "-t", str(duration), "-c:v", "libx264", "-c:a", "aac",
        "-movflags", "+faststart", output_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if result.returncode != 0:
        print(f"  [Error] ffmpeg failed: {result.stderr[:200]}")
        return False
    return True

def default_output_dir():
    return f"outputs/{datetime.now(timezone.utc).strftime('%Y-%m-%d')}/clips"

def cut_all(video_path, cuts, output_dir=None, ffmpeg_path=None):
    if ffmpeg_path is None:
        ffmpeg_path = find_ffmpeg()
    if output_dir is None:
        output_dir = default_output_dir()
    if not os.path.exists(video_path):
        print(f"Error: video not found: {video_path}")
        return
    os.makedirs(output_dir, exist_ok=True)
    for i, cut in enumerate(cuts):
        start = cut.get("start_time", "")
        end = cut.get("end_time", "")
        title = cut.get("title", f"cut_{i+1}")
        safe_title = "".join(c if c.isprintable() and c not in '<>:"/\\|?*\x00' else "_" for c in title)[:50]
        out_name = f"{safe_title}.mp4"
        out_path = os.path.join(output_dir, out_name)
        print(f"Cutting {i+1}/{len(cuts)}: {title} ({start}->{end})")
        ok = cut_clip(video_path, start, end, out_path, ffmpeg_path)
        if ok:
            print(f"  -> {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cut video clips by timestamp")
    parser.add_argument("video", help="path to source .mp4")
    parser.add_argument("--cuts", help="path to Excel .xlsx with cuts")
    parser.add_argument("--cuts-json", help="JSON string or file with cuts array")
    parser.add_argument("--output", default=None, help="output directory (default: outputs/YYYY-MM-DD/clips/)")
    parser.add_argument("--ffmpeg", default=None, help="ffmpeg path (auto-detected if omitted)")
    args = parser.parse_args()

    cuts = []
    if args.cuts_json:
        if os.path.exists(args.cuts_json):
            with open(args.cuts_json, "r", encoding="utf-8-sig") as f:
                cuts = json.load(f)
        else:
            raw = args.cuts_json
            if raw.startswith("'") and raw.endswith("'"):
                raw = raw[1:-1]
            cuts = json.loads(raw)
    elif args.cuts:
        import openpyxl
        wb = openpyxl.load_workbook(args.cuts)
        ws = wb.active
        for row in ws.iter_rows(min_row=2, values_only=True):
            if row[3] and row[4]:
                cuts.append({
                    "title": row[2] or f"cut_{row[0]}",
                    "start_time": row[3],
                    "end_time": row[4],
                })
    else:
        print("Usage: python scripts/cut_clips.py <video.mp4> --cuts <cuts.xlsx> --output clips/")
        sys.exit(1)

    cut_all(args.video, cuts, args.output, args.ffmpeg)