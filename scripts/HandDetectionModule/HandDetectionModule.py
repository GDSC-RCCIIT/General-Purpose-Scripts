import cv2 as cv
import mediapipe as mp
import time
import math


class handDetector:
    def __init__(self, mode=False, max_hands=2, decetion_conf=0.5, tracking_conf=0.5):
        """
        Init method

        params :
            mode : bool
            If set to false, the solution treats the input images as a video stream. It will try to detect hands in the first input images,
            and upon a successful detection further localizes the hand landmarks, If set to true, hand detection runs on every input image, ideal for processing a batch of static,
            possibly unrelated, images. Default to false.

            max_hands : int
            maximum number of hands that can be detected, default set to 2.

            decetion_conf : double [0.0, 1.0]
            Minimum confidence value ([0.0, 1.0]) from the hand detection model for the detection to be considered successful. Default to 0.5.

            trackint_conf : double [0.0, 1.0]
            Minimum confidence value ([0.0, 1.0]) from the landmark-tracking model for the hand landmarks to be considered tracked successfully,
            or otherwise hand detection will be invoked automatically on the next input image. Default set to 0.5.
        """

        self.mode = mode
        self.max_hands = max_hands
        self.decetion_conf = decetion_conf
        self.tracking_conf = tracking_conf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.max_hands, self.decetion_conf, self.tracking_conf
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):

        """
        Detects if hands on the screen and draws outline if draw is true.

        params :
            img : an image stream.
            draw : bool
                Draws outline of hand if true. Default is true.

        return : Image with outline if draw is true.
        """

        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)

        if self.result.multi_hand_landmarks:
            for handlms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handlms, self.mpHands.HAND_CONNECTIONS
                    )
        return img

    def getPosition(self, img, handNo=0, draw=False):
        """
        img : an image upstream.
        handNo : 0 for left hand and 1 for right hand.
        draw : bool

        returns : A list of [id, x-corrdinate, y-coordinate] where id represents points on fingers (see documentation).
        """

        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(w * lm.x), int(h * lm.y)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 6, (255, 255, 255), -1)
        return lmList


## A sample Implementation.
def main():
    capture = cv.VideoCapture(0)
    pTime = 0
    cTime = 0

    detector = handDetector(decetion_conf=0.75, tracking_conf=0.65)
    while True:
        isTrue, img = capture.read()
        img = detector.findHands(img)
        lmList = detector.getPosition(img, draw=False)

        if len(lmList) != 0:
            print(lmList)

        # Shows FPS (Frame per second) on screen.
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_ITALIC, 2, (0, 0, 0), 3)

        cv.imshow("WebCam", img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()
