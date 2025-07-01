from pydub import AudioSegment
from pathlib import Path


def trim_audio_by_time(
        input_path,
        output_path=None,
        trim_start_sec=0,
        trim_end_sec=0,
):

    input_path = Path(input_path)
    audio = AudioSegment.from_file(input_path)

    start_ms = trim_start_sec * 1000
    end_trim_ms = trim_end_sec * 1000
    end_ms = len(audio) - end_trim_ms if trim_end_sec > 0 else None

    trimmed = audio[start_ms:end_ms]

    output_path = output_path or input_path
    trimmed.export(output_path, format="mp3")
    print(f"Trimmed {input_path.name}: -{trim_start_sec}s start, -{trim_end_sec}s end")
    return output_path
