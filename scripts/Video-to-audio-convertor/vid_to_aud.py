import moviepy.editor
from moviepy.video.VideoClip import VideoClip
from pathlib import Path

a = input("Enter the path of the video:\n")
video = moviepy.editor.VideoFileClip(a)
p = Path(a)
if p.exists():
    video = moviepy.editor.VideoFileClip(a)

    # to create the audio file:

    audio = video.audio
    audio.write_audiofile("extractedaudio.mp3")
    # audio will be saved as extractedaudio.mp3 in the current directory.
