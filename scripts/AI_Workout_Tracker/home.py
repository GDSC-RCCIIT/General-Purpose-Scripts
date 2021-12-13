# Created by @nipunarora8
from tkinter import *
from PIL import ImageTk, Image
import cv2
import mediapipe as mp
import imageio
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
from mediapipe.python.solutions.pose import PoseLandmark
from exercise import workout

import os

base_dir = os.path.dirname(os.path.realpath(__file__))

root = Tk()
root.attributes("-fullscreen", True)
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root["bg"] = "black"


def opencameraWindow():
    lst = []
    global cam_bg, startt_btn, stop_btn, camera_window, imgcanvas, begin
    stop = True

    def start_camera():

        lvid = Label(vidcanvas)
        lvid.grid(row=0, column=0)

        lstick = Label(imgcanvas)
        lstick.grid(row=0, column=0)
        global cap
        cap = cv2.VideoCapture(0)
        # imgcanvas.create_image(0,0, anchor=NW, image=img)
        def show_frame():
            with mp_pose.Pose(
                min_detection_confidence=0.5, min_tracking_confidence=0.5
            ) as pose:
                try:
                    _, frame = cap.read()
                    frame = cv2.flip(frame, 1)
                    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    cv2image.flags.writeable = False
                    cv2image = cv2.resize(cv2image, (700, 550))
                    cv2image, blank_image = workout(cv2image, pose)

                    img = Image.fromarray(cv2image)
                    imgtk = ImageTk.PhotoImage(image=img)
                    lvid.imgtk = imgtk
                    lvid.configure(image=imgtk)

                    img_stick = Image.fromarray(blank_image)
                    imgst = ImageTk.PhotoImage(image=img_stick)
                    lstick.imgtk = imgst
                    lstick.configure(image=imgst)
                    lstick.after(20, show_frame)
                except:
                    pass

        if stop:
            show_frame()

    def stop_camera():
        try:
            cap.release()
        except NameError:
            pass
        quit()

    # Toplevel object which will
    # be treated as a new window
    camera_window = Toplevel(root)

    camera_window.title("Workout Tracker")
    camera_window.attributes("-fullscreen", True)

    # sets the geometry of toplevel
    camera_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

    cam_bg = PhotoImage(file=f"{base_dir}/resources/camera_bg.png")
    bg_cam = Label(camera_window, image=cam_bg)
    bg_cam.place(x=0, y=0, relwidth=1, relheight=1)

    imgcanvas = Canvas(
        camera_window,
        width=700,
        height=550,
        bg="black",
        highlightthickness=3,
        highlightbackground="white",
    )
    imgcanvas.place(x=40, y=140)
    begin = PhotoImage(file=f"{base_dir}/resources/begin.png")
    labell = Label(imgcanvas, image=begin)
    labell["bg"] = "black"
    labell["border"] = "0"
    labell.place(x=110, y=220)

    vidcanvas = Canvas(
        camera_window,
        width=700,
        height=550,
        bg="black",
        highlightthickness=3,
        highlightbackground="white",
    )
    vidcanvas.place(x=800, y=140)
    labelr = Label(vidcanvas, image=begin)
    labelr["bg"] = "black"
    labelr["border"] = "0"
    labelr.place(x=110, y=220)

    # buttons
    startt_btn = PhotoImage(file=f"{base_dir}/resources/start_video.png")
    btn_startt = Button(camera_window, image=startt_btn, command=start_camera)
    btn_startt["bg"] = "#2A2D2C"
    btn_startt["border"] = "0"
    btn_startt.place(x=300, y=725)

    stop_btn = PhotoImage(file=f"{base_dir}/resources/stop_video.png")
    btn_stop = Button(camera_window, image=stop_btn, command=stop_camera)
    btn_stop["bg"] = "#232525"
    btn_stop["border"] = "0"
    btn_stop.place(x=1000, y=725)

    camera_window.bind("<Key-Escape>", quit)


bg = PhotoImage(file=f"{base_dir}/resources/main_screen.png")

bg_img = Label(root, image=bg)
bg_img.place(x=0, y=0, relwidth=1, relheight=1)

start_btn = PhotoImage(file=f"{base_dir}/resources/Start Button.png")
btn_start = Button(root, text="clickme", image=start_btn, command=opencameraWindow)
btn_start["bg"] = "#202020"
btn_start["border"] = "0"
btn_start.place(x=670, y=561)

root.bind("<Key-Escape>", quit)

root.mainloop()
