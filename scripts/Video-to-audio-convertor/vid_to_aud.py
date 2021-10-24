import moviepy.editor
from moviepy.video.VideoClip import VideoClip
from pathlib import Path

# To take path of the video as input

a = input("Enter the path of the video:\n")     # Enter path of the video in the terminal.

video = moviepy.editor.VideoFileClip(a)
p = Path(a)
if p.exists():
    video = moviepy.editor.VideoFileClip(a)

    # to create the audio file:

    audio = video.audio
    audio.write_audiofile("extractedaudio.mp3")
    # audio will be saved as extractedaudio.mp3 in the current directory.
