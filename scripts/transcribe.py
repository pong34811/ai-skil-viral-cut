import os
import subprocess
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    except ImportError:
        pass

client = Groq(api_key=GROQ_API_KEY)


def extract_audio(mp4_path):
    audio_path = mp4_path.replace(".mp4", ".wav")
    subprocess.run(
        ["ffmpeg", "-i", mp4_path, "-vn", "-ar", "16000", "-ac", "1", "-y", audio_path],
        check=True, capture_output=True
    )
    return audio_path


def transcribe(mp4_path, model="whisper-large-v3", response_format="srt", language="th"):
    audio_path = extract_audio(mp4_path)

    with open(audio_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            file=(os.path.basename(audio_path), f.read()),
            model=model,
            response_format=response_format,
            language=language,
        )

    srt_path = mp4_path.replace(".mp4", ".srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(transcription)

    os.remove(audio_path)
    return srt_path


if __name__ == "__main__":
    import glob
    mp4_files = glob.glob("raw/*.mp4")
    if not mp4_files:
        print("No .mp4 files found in raw/")
    else:
        for mp4 in mp4_files:
            print(f"Transcribing: {mp4}")
            srt = transcribe(mp4)
            print(f"Saved: {srt}")
