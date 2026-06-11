import os, sys, math, json, subprocess, time
from dotenv import load_dotenv
from tqdm import tqdm
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(script_dir, '..', '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv('GROQ_API_KEY')
API_URL = "https://api.groq.com/openai/v1/audio/transcriptions"

MAX_SIZE_BYTES = 24 * 1024 * 1024

def format_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"

def get_groq_data(file_path, file_bytes, word_level=False):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "whisper-large-v3",
        "temperature": 0,
        "response_format": "verbose_json",
    }
    if word_level:
        data["timestamp_granularities"] = ["word"]
    files = {"file": (os.path.basename(file_path), file_bytes, "audio/mpeg" if file_path.endswith('.mp3') else "audio/wav")}
    try:
        resp = requests.post(API_URL, headers=headers, data=data, files=files, timeout=300)
        resp.raise_for_status()
        result = resp.json()
        return result.get('segments') or [], result.get('words') or []
    except Exception as e:
        print(f"\n[API Error] {os.path.basename(file_path)}: {e}")
        return [], []

def process_file(filename, request_word_timestamps, export_srt, export_json):
    file_size = os.path.getsize(filename)
    all_segments = []
    all_words = []

    if file_size <= MAX_SIZE_BYTES:
        with tqdm(total=1, desc="Transcribing file", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}]") as pbar:
            with open(filename, "rb") as f:
                all_segments, all_words = get_groq_data(filename, f.read(), word_level=request_word_timestamps)
            pbar.update(1)
    else:
        print("File is larger than 25MB. Pre-processing audio chunks...")
        chunk_length_sec = 10 * 60
        probe_cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", filename
        ]
        result = subprocess.run(probe_cmd, capture_output=True, text=True)
        total_duration_sec = float(result.stdout.strip())
        num_chunks = math.ceil(total_duration_sec / chunk_length_sec)

        with tqdm(total=num_chunks, desc="Processing video chunks", unit="chunk") as pbar:
            for i in range(num_chunks):
                start_time_sec = i * chunk_length_sec
                end_time_sec = min(start_time_sec + chunk_length_sec, total_duration_sec)
                temp_chunk_path = os.path.join(script_dir, f"temp_chunk_{i}.mp3")
                ffmpeg_cmd = [
                    "ffmpeg", "-y", "-ss", str(start_time_sec),
                    "-i", filename, "-t", str(end_time_sec - start_time_sec),
                    "-vn", "-acodec", "libmp3lame", "-b:a", "64k",
                    temp_chunk_path
                ]
                subprocess.run(ffmpeg_cmd, capture_output=True, check=True)
                with open(temp_chunk_path, "rb") as f:
                    chunk_segs, chunk_wds = get_groq_data(temp_chunk_path, f.read(), word_level=request_word_timestamps)
                for seg in chunk_segs:
                    seg['start'] += start_time_sec
                    seg['end'] += start_time_sec
                    all_segments.append(seg)
                for wd in chunk_wds:
                    wd['start'] += start_time_sec
                    wd['end'] += start_time_sec
                    all_words.append(wd)
                if os.path.exists(temp_chunk_path):
                    os.remove(temp_chunk_path)
                pbar.update(1)

    if not all_words and all_segments:
        for seg in all_segments:
            if 'words' in seg:
                all_words.extend(seg['words'])

    base_path, _ = os.path.splitext(filename)
    print(f"\nProcessing complete! Generating requested files:")

    if export_srt:
        srt_path = f"{base_path}.srt"
        with open(srt_path, "w", encoding="utf-8") as f:
            for idx, seg in enumerate(all_segments, 1):
                f.write(f"{idx}\n")
                f.write(f"{format_srt_time(seg['start'])} --> {format_srt_time(seg['end'])}\n")
                f.write(f"{seg['text'].strip()}\n\n")
        print(f" - Created: {os.path.basename(srt_path)}")

    if export_json:
        json_path = f"{base_path}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({"segments": all_segments, "words": all_words}, f, indent=2)
        print(f" - Created: {os.path.basename(json_path)}")

if __name__ == "__main__":
    args = sys.argv[1:]
    flags = [arg for arg in args if arg.startswith('--')]
    positional_args = [arg for arg in args if not arg.startswith('--')]

    if not positional_args:
        mp4_files = [os.path.join("raw", f) for f in os.listdir("raw") if f.endswith(".mp4")]
        if not mp4_files:
            print("Error: No .mp4 files found in raw/")
            sys.exit(1)
        filenames = mp4_files
    else:
        filenames = [os.path.abspath(arg) for arg in positional_args]

    export_srt = '--srt' in flags or not any(f in flags for f in ['--srt', '--json'])
    export_json = '--json' in flags
    request_word_timestamps = '--word-by-word' in flags

    for fname in filenames:
        if not os.path.exists(fname):
            print(f"Error: File '{fname}' not found.")
            continue
        print(f"Transcribing: {fname}")
        process_file(fname, request_word_timestamps, export_srt, export_json)
