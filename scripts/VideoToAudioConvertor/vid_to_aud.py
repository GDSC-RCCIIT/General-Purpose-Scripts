import moviepy.editor
from moviepy.video.VideoClip import VideoClip

# to select the video file:

video = moviepy.editor.VideoFileClip(" ")   # Add path of your your video in between the inverted commas.

# to create the audio file:

audio = video.audio
audio.write_audiofile("extractedaudio.mp3")  # audio will be saved as extractedaudio.mp3 in the current directory.
