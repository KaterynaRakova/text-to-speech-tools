from pathlib import Path
from pydub import AudioSegment

def generate_silence(pause_sec=1.0):

    return AudioSegment.silent(duration=int(pause_sec * 1000))
from pathlib import Path
from pydub import AudioSegment
from tts.merge import generate_silence  # если в том же файле — можно опустить импорт

def merge_audio(files, output_path, add_pause=False, pause_sec=1.0):

    combined = AudioSegment.empty()
    pause = generate_silence(pause_sec) if add_pause else AudioSegment.empty()

    for idx, file_path in enumerate(files):
        file_path = Path(file_path)
        if not file_path.exists():
            print(f"file not found: {file_path}")
            continue

        print(f" Add: {file_path.name}")
        audio = AudioSegment.from_file(file_path)

        combined += audio
        if add_pause and idx < len(files) - 1:
            combined += pause

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    combined.export(output_path, format="mp3")
    print(f"Merged file save at: {output_path}")
    return output_path

