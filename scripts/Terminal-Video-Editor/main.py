import os
from moviepy.editor import *

bool_video = False
bool_Audio = False
bool_gif = False
bool_prevloopinput = False

# ==================================================== PATH
video_path = input("Enter : Path of the video\n>> ")
Path_Exist = os.path.isfile(video_path)
if Path_Exist == False:
    print("Wrong Path Input")
    quit()
extension = video_path[-4:]
if extension != ".mp4":
    print("Currently Only mp4 Files can be edited")
    quit()

# ==================================================== LOAD VIDEO
clip = VideoFileClip(video_path)

name = clip.filename
rate = clip.fps
Size = os.path.getsize(video_path) / (1024 * 1024)
Size = round(float(Size), 2)
duration = clip.duration
width_before = clip.w
height_before = clip.h

name_1 = name.split("/")
name_2 = name_1[-1]

if duration < 600 and duration > 0:
    # =================================================== PRINT VIDEO DETAILS
    print("\n-----------------------------------------------------")
    print("File Name  : " + name_2)
    print("FPS : " + str(rate))
    print("Size : " + str(Size) + " MB")
    print("Duration : " + str(duration) + " s")
    print("Width x Height : " + str(width_before) + " x " + str(height_before))
    print("-----------------------------------------------------\n")
else:
    print("Sorry but currently we are supporting video duration max : 10 minute")
    quit()

# ==================================================== PATH
input1 = input(
    "Enter \n\t<1> To Edit Video (Single Step)\n\t<2> To Edit Video (Multiple Step)\n\t<3> To Extract Audio from Video\n\t<4> To Convert Video into GIF\n>> "
)

# ==================================================== Edit Video Single Step
if input1 == "1":
    bool_video = True
    input2 = input(
        "Enter \n\t<1> To Trim Video\n\t<2> To Cutout a portion from Video\n\t<3> To Resize Video\n\t<4> To Change Playback Speed\n\t<5> To Control Volume (in %)\n>> "
    )

    # ==================================================== Trim
    if input2 == "1":
        input3 = input(
            "Enter :\n\t<1> To Trim From Beginning\n\t<2> To Trim From Ending\n\t<3> For Custom Trim\n>> "
        )

        # ==================================================== From Starting
        if input3 == "1":
            start_input = input("Enter Starting Point (in sec) :\n>> ")
            start = float(start_input)
            if start < duration and start > 0:
                clip = clip.subclip(start, duration)
                print("Trimming...")
            else:
                print("Starting Point should be > 0 and < " + str(duration))

        # ==================================================== From Ending
        elif input3 == "2":
            end_input = input("Enter Ending Point (in sec) :\n>> ")
            end = float(end_input)
            if end < duration and end > 0:
                clip = clip.subclip(0, end)
                print("Trimming...")
            else:
                print("Ending Point should be > 0 and < " + str(duration))

        # ==================================================== Custom trim
        elif input3 == "3":
            start_input = input("Enter Starting Point (in sec) :\n>> ")
            start = float(start_input)
            if start < duration and start >= 0:
                end_input = input("Enter Ending Point (in sec) :\n>> ")
                if end_input < duration and end_input > 0:
                    end = float(end_input)
                    clip = clip.subclip(start, end)
                    print("Trimming...")
                else:
                    print("Ending Point should be > 0 and < " + str(duration))
            else:
                print("Starting Point should be >= 0 and < " + str(duration))

        # ==================================================== Wrong Input
        else:
            print("Wrong Input")
            quit()

    # ==================================================== Cut
    elif input2 == "2":
        start_input = input("Enter Starting Point (in sec) :\n>> ")
        start = float(start_input)
        if start < duration and start >= 0:
            end_input = input("Enter Ending Point (in sec) :\n>> ")
            end_input = float(end_input)
            if end_input < duration and end_input > 0:
                end = end_input
                clip = clip.cutout(start, end)
                print("Cutting Out...")
            else:
                print("Ending Point should be > 0 and <= " + str(duration))
        else:
            print("Starting Point should be >= 0 and < " + str(duration))

    # ==================================================== Resize
    elif input2 == "3":
        rezise_percentage = input(
            "Enter how much you want to compress \n(Min: 1% || Max: 99%)\n>> "
        )
        rezise_percentage = float(rezise_percentage)
        if rezise_percentage > 0 and rezise_percentage < 100:
            rezise_percentage = float(rezise_percentage / 100)
            clip = clip.resize(rezise_percentage)
            print("Resizing...")
        else:
            print("Value Should be within 1% - 99%")

    # ==================================================== Speed
    elif input2 == "4":
        speed_input = input("Enter video speed you want :\n(Min: 0.2x || Max: 5x)\n>> ")
        speed_input = float(speed_input)
        if speed_input >= 0.2 and speed_input <= 5:
            clip = clip.fx(vfx.speedx, speed_input)
            print("Changing Speed...")
        else:
            print("Value Should be within 0.2x - 5x")

    # ==================================================== Volume
    elif input2 == "5":
        volume_percentage = input(
            "Enter how much volume want :\n(Min: 0.1x || Max: 3x || Note: More than 1x may distorted te audio)\n>> "
        )
        volume_percentage = float(volume_percentage)
        if volume_percentage >= 0.1 and volume_percentage <= 3:
            clip = clip.volumex(volume_percentage)
            print("Changing Volume...")
        else:
            print("Value Should be within 0.1x - 3x")
    else:
        print("Wrong Input")

# ==================================================== Edit Video Multiple Step
elif input1 == "2":
    close = False
    bool_video = True
    while close == False:
        input4 = input(
            "Press : \n\t<0> To End Process\nEnter \n\t<1> To Trim Video\n\t<2> To Cutout a portion from Video\n\t<3> To Resize Video\n\t<4> To Change Playback Speed\n\t<5> To Control Volume (in %)\n>> "
        )

        # ==================================================== End
        if input4 == "0":
            if bool_prevloopinput == False:
                print("No Change")
                quit()
            close = True

        # ==================================================== Trim
        elif input4 == "1":
            bool_prevloopinput = True
            input5 = input(
                "Enter :\n\t<1> To Trim From Beginning\n\t<2> To Trim From Ending\n\t<3> For Custom Trim\n>> "
            )

            # ==================================================== From Starting
            if input5 == "1":
                start_input = input("Enter Starting Point (in sec) :\n>> ")
                start = float(start_input)
                if start < duration and start > 0:
                    clip = clip.subclip(start, duration)
                    print("Trimming...")
                else:
                    print("Starting Point should be > 0 and < " + str(duration))

            # ==================================================== From Ending
            elif input5 == "2":
                end_input = input("Enter Ending Point (in sec) :\n>> ")
                end = float(end_input)
                if end < duration and end > 0:
                    clip = clip.subclip(0, end)
                    print("Trimming...")
                else:
                    print("Ending Point should be > 0 and < " + str(duration))

            # ==================================================== Custom Trim
            elif input5 == "3":
                start_input = input("Enter Starting Point (in sec) :\n>> ")
                start = float(start_input)
                if start < duration and start >= 0:
                    end_input = input("Enter Ending Point (in sec) :\n>> ")
                    end_input = float(end_input)
                    if end_input < duration and end_input > 0:
                        end = float(end_input)
                        clip = clip.subclip(start, end)
                        print("Trimming...")
                    else:
                        print("Ending Point should be > 0 and < " + str(duration))
                else:
                    print("Starting Point should be >= 0 and < " + str(duration))
            else:
                print("Wrong Input")

        # ==================================================== Cutout
        elif input4 == "2":
            bool_prevloopinput = True
            start_input = input("Enter Starting Point (in sec) :\n>> ")
            start = float(start_input)
            if start < duration and start >= 0:
                end_input = input("Enter Ending Point (in sec) :\n>> ")
                end_input = float(end_input)
                if end_input <= duration and end_input > 0:
                    end = float(end_input)
                    clip = clip.cutout(start, end)
                    print("Cutting Out...")
                else:
                    print("Ending Point should be > 0 and <= " + str(duration))
            else:
                print("Starting Point should be >= 0 and < " + str(duration))

        # ==================================================== Resize
        elif input4 == "3":
            bool_prevloopinput = True
            rezise_percentage = input(
                "Enter how much you want to compress \n(Min: 1% || Max: 99%)\n>> "
            )
            rezise_percentage = float(rezise_percentage)
            if rezise_percentage > 0 and rezise_percentage < 100:
                rezise_percentage = float(rezise_percentage / 100)
                clip = clip.resize(rezise_percentage)
                print("Resizing...")
            else:
                print("Value Should be within 1% - 99%")

        # ==================================================== Speed Control
        elif input4 == "4":
            bool_prevloopinput = True
            speed_input = input(
                "Enter video speed you want :\n(Min: 0.2x || Max: 5x)\n>> "
            )
            speed_input = float(speed_input)
            if speed_input >= 0.2 and speed_input <= 5:
                clip = clip.fx(vfx.speedx, speed_input)
                print("Changing Speed...")
            else:
                print("Value Should be within 0.2x - 5x")

        # ==================================================== Volume
        elif input4 == "5":
            bool_prevloopinput = True
            volume_percentage = input(
                "Enter how much volume want :\n(Min: 0.1x || Max: 3x || Note: More than 1x may distorted te audio)\n>> "
            )
            volume_percentage = float(volume_percentage)
            if volume_percentage >= 0.1 and volume_percentage <= 3:
                clip = clip.volumex(volume_percentage)
                print("Changing Volume...")
            else:
                print("Value Should be within 0.1x - 3x")
        else:
            print("Wrong Input")

# ==================================================== Extract Audio
elif input1 == "3":
    bool_Audio = True
    clip = clip.audio
    print("Extracting Audio...")

# ==================================================== Convert Video to GIF
elif input1 == "4":
    start_input = input("Enter Starting Point (in sec) :\n>> ")
    start = float(start_input)
    if start < duration and start >= 0:
        gif_time = input(
            "Enter how long the GIF you want to be (in sec) (Max: 6sec):\n>> "
        )
        gif_time = float(gif_time)
        if gif_time < 6 and gif_time > 0:
            end = start + gif_time
            if end > duration:
                end = duration
            clip = clip.subclip(start, end).resize(0.5)
    bool_gif = True
    print("Converting to GIF...")

# ==================================================== Wrong Input
else:
    print("Wrong Input")
    quit()

# ==================================================== Audio
if bool_Audio == True:
    clip.write_audiofile("Audio-TVE-GDSC-RCCIIT.mp3")
    bool_Audio = False

# ==================================================== GIF
if bool_gif == True:
    clip.write_gif("GIF-TVE-GDSC-RCCIIT.gif")
    bool_gif == False

# ==================================================== Video
if bool_video == True:
    clip.write_videofile(
        "Video-TVE-GDSC-RCCIIT.mp4",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
    )
    bool_video == False
