# main.py

import asyncio
from tts.speak import speak_text_to_mp3
from tts.filename_utils import  get_next_filename


def read_text_file(filepath):
    with open(filepath,"r", encoding="utf-8") as file:
        return file.read()

if __name__ == "__main__":
    text = read_text_file("texts/chapter1.txt")
    asyncio.run(speak_text_to_mp3(text,get_next_filename(base_name="chapter")))