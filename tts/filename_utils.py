import os

def get_next_filename(folder="output", base_name="piece", ext=".mp3"):

    i = 1
    while True:
        filename = os.path.join(folder, f"{base_name}{i}{ext}")
        if not os.path.exists(filename):
            return filename
        i += 1