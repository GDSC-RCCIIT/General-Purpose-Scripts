import cv2
import time
import mediapipe as pipe
import HandTrackingModule as htm
import numpy as np
import math
import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

capture = cv2.VideoCapture(0)

cTime = 0
pTime = 0

detector = htm.handDetector(maxHands=1)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = capture.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, box = detector.finPosition(img, draw=True)

    if len(lmList) != 0:
        length, img, lineInfo = detector.findDistance(4, 8, img)
        volBar = np.interp(length, [30, 150], [400, 150])
        volPer = np.interp(length, [30, 150], [0, 100])

        smoothness = 5
        volPer = smoothness * round(volPer / smoothness)

        fingers = detector.fingersUp()
        if not fingers[4]:
            volume.SetMasterVolumeLevelScalar(volPer / 100, None)
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(
        img,
        str(int(volPer)),
        (10, 450),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        2,
        (255, 255, 255),
        3,
    )

    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    pTime = cTime

    cv2.putText(
        img, str(fps), (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 0, 255), 3
    )

    cv2.imshow("Feed", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
