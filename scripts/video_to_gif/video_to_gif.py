from moviepy.editor import *

clip = (VideoFileClip("filename.extension(like mp4)").subclip((0.2),(0.5))) #subclip((starting time from the video for gif),(ending time)))
clip.write_gif("output.gif")                                                #output file name will be output.gif
print("completed")
