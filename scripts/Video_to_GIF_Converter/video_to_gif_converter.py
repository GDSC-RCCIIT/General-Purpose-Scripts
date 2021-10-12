from moviepy.editor import VideoFileClip
from tkinter.filedialog import *


# ---------------function to get the time frames for the GIF----------
def gif_time():
    print(
        "\nEnter time in the format: minutes seconds (Example: 2 2.5 --> 2 minutes 2.5 seconds)"
    )
    start = list(map(float, input("GIF start time: --> ").split()))
    end = list(map(float, input("GIF end time: --> ").split()))
    if len(start) == 1:
        start.append(0)
    if len(end) == 1:
        end.append(0)

    return start, end


try:
    video = askopenfilename()

    while not video:
        video = askopenfilename()

    # ---------calls the function------------
    clip_start, clip_end = gif_time()

    # -------condition to check if start time in minutes > end time------
    while clip_start[0] > clip_end[0]:
        print("\nYou have entered start time > end time, which is not supported\n")
        clip_start, clip_end = gif_time()

    # -------2nd condition to check if start time in seconds> end time------
    while clip_start[0] == clip_end[0] and clip_start[1] > clip_end[1]:
        print("\nYou have entered start time > end time, which is not supported\n")
        clip_start, clip_end = gif_time()

    # -------condition to check if start time is equal to end time------
    while "".join(str(clip_start)) == "".join(str(clip_end)):
        print("\nYou have entered start time == end time, which is not supported\n")
        clip_start, clip_end = gif_time()

    # ----------Get the size of the GIF image from user----------------
    resize = float(input("\nGIF size ( > 0 and < 1 preferred )(Example: 0.2): --> "))

    print("\nProcessing...")

    # ----------convert video to GIF with the given time frames----------------
    clip = (
        VideoFileClip(video)
        .subclip((clip_start[0], clip_start[1]), (clip_end[0], clip_end[1]))
        .resize(resize)
    )

    clip.write_gif("mygif.gif")

    print(
        """
    ***************************************
    mygif.gif created (check the .gif file)
    ***************************************"""
    )

# -------------print exceptions-----------------
except Exception as e:
    print("\nError occurred: ", e)

# -------------Keyboard exception-----------------
except KeyboardInterrupt:
    print("\nError occurred: KeyboardInterrupt")
