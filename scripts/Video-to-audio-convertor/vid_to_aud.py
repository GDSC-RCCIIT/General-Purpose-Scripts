import moviepy.editor
from moviepy.video.VideoClip import VideoClip

# to select the video file:
a = input("Enter the path of the video:\n")
video = moviepy.editor.VideoFileClip(
    a
)  # Add path of your video in the terminal

# to create the audio file:

audio = video.audio
audio.write_audiofile(
    "extractedaudio.mp3"
)  # audio will be saved as extractedaudio.mp3 in the current directory.
