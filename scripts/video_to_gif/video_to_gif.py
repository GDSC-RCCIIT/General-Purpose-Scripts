from moviepy.editor import *

clip = (VideoFileClip("filename.extension(like mp4)").subclip((0.2),(0.5))) 
clip.write_gif("output.gif")  #name of the output file will be output.gif
print("completed")
