print("Importing...")
from os import mkdir, listdir
from moviepy.editor import AudioFileClip

try:
    mkdir("audio files")
except:
    pass

input("Put all audio files in audio files folder and then press enter...")

try:
    mkdir("result")
except:
    pass

print("Getting audio files...")
audio_files = []
file_names = []
for file in listdir("./audio files"):
    file_names.append(file)
    audio_file = AudioFileClip(f"./audio files/{file}")
    audio_files.append(audio_file)

print("Writing files...")
for index, audio_file in enumerate(audio_files):
    file_name = file_names[index][:-4]
    audio_file.write_audiofile(f"./result/{file_name}.mp3")
print("Done...")
