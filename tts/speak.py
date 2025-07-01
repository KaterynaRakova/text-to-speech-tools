import asyncio
import edge_tts

async def speak_text_to_mp3(text: str, filename: str = "output/output.mp3", voice: str = "ru-RU-SvetlanaNeural"):

    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(filename)
    print(f"✅ Saved: {filename}")