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

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

POSE_CONNECTIONS = frozenset([
    (PoseLandmark.RIGHT_SHOULDER, PoseLandmark.LEFT_SHOULDER),
    (PoseLandmark.RIGHT_SHOULDER, PoseLandmark.RIGHT_ELBOW),
    (PoseLandmark.RIGHT_ELBOW, PoseLandmark.RIGHT_WRIST),
    (PoseLandmark.LEFT_SHOULDER, PoseLandmark.LEFT_ELBOW),
    (PoseLandmark.LEFT_ELBOW, PoseLandmark.LEFT_WRIST),
    (PoseLandmark.LEFT_ELBOW, PoseLandmark.LEFT_WRIST),
    (PoseLandmark.RIGHT_ELBOW, PoseLandmark.RIGHT_WRIST),
    (PoseLandmark.LEFT_WRIST, PoseLandmark.LEFT_PINKY),
    (PoseLandmark.LEFT_WRIST, PoseLandmark.LEFT_INDEX),
    (PoseLandmark.LEFT_WRIST, PoseLandmark.LEFT_THUMB),
    (PoseLandmark.RIGHT_WRIST, PoseLandmark.RIGHT_PINKY),
    (PoseLandmark.RIGHT_WRIST, PoseLandmark.RIGHT_INDEX),
    (PoseLandmark.RIGHT_WRIST, PoseLandmark.RIGHT_THUMB),
    (PoseLandmark.LEFT_PINKY, PoseLandmark.LEFT_INDEX),
    (PoseLandmark.RIGHT_PINKY, PoseLandmark.RIGHT_INDEX),
    (PoseLandmark.RIGHT_SHOULDER, PoseLandmark.RIGHT_HIP),
    (PoseLandmark.LEFT_SHOULDER, PoseLandmark.LEFT_HIP),
    (PoseLandmark.RIGHT_HIP, PoseLandmark.LEFT_HIP),
    (PoseLandmark.RIGHT_HIP, PoseLandmark.LEFT_HIP),
    (PoseLandmark.LEFT_HIP, PoseLandmark.LEFT_KNEE),
    (PoseLandmark.RIGHT_HIP, PoseLandmark.LEFT_HIP),
    (PoseLandmark.RIGHT_HIP, PoseLandmark.RIGHT_KNEE),
    (PoseLandmark.LEFT_KNEE, PoseLandmark.LEFT_ANKLE),
    (PoseLandmark.RIGHT_KNEE, PoseLandmark.RIGHT_ANKLE),
    (PoseLandmark.LEFT_ANKLE, PoseLandmark.LEFT_HEEL),
    (PoseLandmark.LEFT_ANKLE, PoseLandmark.LEFT_FOOT_INDEX),
    (PoseLandmark.RIGHT_ANKLE, PoseLandmark.RIGHT_HEEL),
    (PoseLandmark.RIGHT_ANKLE, PoseLandmark.RIGHT_FOOT_INDEX),
    (PoseLandmark.LEFT_HEEL, PoseLandmark.LEFT_FOOT_INDEX),
    (PoseLandmark.RIGHT_HEEL, PoseLandmark.RIGHT_FOOT_INDEX)
])

def angle_cal(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    #vector_calculation
    v_1 = np.array([a[0]-b[0],a[1]-b[1]])
    v_2 = np.array([c[0]-b[0],c[1]-b[1]])
    
    cos_theta = np.dot(v_1,v_2)/(np.linalg.norm(v_1)*np.linalg.norm(v_2))
    angle_radian = np.arccos(cos_theta)
    angle = int(np.abs(angle_radian*57.2958))
    
    if angle >180.0:
            angle = 360-angle
            
    return angle

def left(landmarks):
    
    # Get coordinates_
    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

    shoulder_angle = angle_cal(hip, shoulder, elbow)
    elbow_angle = angle_cal(shoulder, elbow, wrist)
        
    return [[shoulder,shoulder_angle],[elbow,elbow_angle]]

def right(landmarks):
    
    # Get coordinates_
    shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
    wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
    hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

    shoulder_angle = angle_cal(hip, shoulder, elbow)
    elbow_angle = angle_cal(shoulder, elbow, wrist)
            
    return [[shoulder,shoulder_angle],[elbow,elbow_angle]]

def visualize(arr,image):
    for i in arr:
        cv2.putText(image, str(i[1]), 
                           tuple(np.multiply(i[0], [700,550]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA
                                )
    
def workout(image,pose):
    ## Setup mediapipe instance        

    results = pose.process(image)
        
    # Recolor back to BGR
    image.flags.writeable = True
    
    blank_image = np.ones((550,700,3), np.uint8)
    # Extract landmarks
    try:
        landmarks = results.pose_landmarks.landmark
                
        visualize(left(landmarks),blank_image)
        visualize(right(landmarks),blank_image)
                
    except:
        pass
            # Render detections
    mp_drawing.draw_landmarks(blank_image, results.pose_landmarks, POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(41,255,249), thickness=1, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(255,255,255), thickness=3, circle_radius=3) 
                                    )
    mp_drawing.draw_landmarks(image, results.pose_landmarks, POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(41,255,249), thickness=1, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(255,255,255), thickness=3, circle_radius=3) 
                                    )            
            
    return image, blank_image

root = Tk()
root.attributes("-fullscreen", True)
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
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
            with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                try: 
                    _, frame = cap.read()
                    frame = cv2.flip(frame, 1)
                    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    cv2image.flags.writeable = False
                    cv2image = cv2.resize(cv2image,(700,550))
                    cv2image, blank_image = workout(cv2image,pose)
                
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
    camera_window.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    
    cam_bg = PhotoImage(file="resources/camera_bg.png")
    bg_cam = Label(camera_window,image=cam_bg)
    bg_cam.place(x=0,y=0,relwidth=1,relheight=1)

    imgcanvas = Canvas(camera_window,width=700, height=550, bg="black", highlightthickness=3, highlightbackground="white")
    imgcanvas.place(x=40,y=140)
    begin = PhotoImage(file="resources/begin.png")
    labell = Label(imgcanvas,image=begin)
    labell["bg"]="black"
    labell["border"] = "0"
    labell.place(x=110,y=220)

    vidcanvas = Canvas(camera_window,width=700, height=550, bg="black", highlightthickness=3, highlightbackground="white")
    vidcanvas.place(x=800,y=140)
    labelr = Label(vidcanvas,image=begin)
    labelr["bg"]="black"
    labelr["border"] = "0"
    labelr.place(x=110,y=220)

    #buttons
    startt_btn = PhotoImage(file="resources/start_video.png")
    btn_startt = Button(camera_window, image = startt_btn, command = start_camera)
    btn_startt["bg"]="#2A2D2C"
    btn_startt["border"] = "0"
    btn_startt.place(x=300,y=725)

    stop_btn = PhotoImage(file="resources/stop_video.png")
    btn_stop = Button(camera_window, image = stop_btn, command = stop_camera)
    btn_stop["bg"]="#232525"
    btn_stop["border"] = "0"
    btn_stop.place(x=1000,y=725)

    camera_window.bind('<Key-Escape>',quit)

bg = PhotoImage(file = "resources/main_screen.png")

bg_img = Label(root,image=bg)
bg_img.place(x=0,y=0,relwidth=1,relheight=1)

start_btn = PhotoImage(file="resources/Start Button.png")
btn_start = Button(root, text = "clickme", image = start_btn,command = opencameraWindow)
btn_start["bg"]="#202020"
btn_start["border"] = "0"
btn_start.place(x=670,y=561)

root.bind('<Key-Escape>',quit)

root.mainloop()
