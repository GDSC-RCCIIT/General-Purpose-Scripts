# pip install cv2-python
# pip install numpy
# pip install pyzbar
import cv2
import numpy
from pyzbar.pyzbar import decode

# capturing image from camera

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# read data (frames) by captured data
while True:
    r, frames = cap.read()

    # decoding the images
    for barcode in decode(frames):
        output = barcode.data.decode("utf-8")
        # geting pos(x1,y1) and pos2(x2,y2) diagonal edge
        pos = numpy.array([barcode.polygon], numpy.int32)
        cv2.polylines(frames, [pos], True, (0, 0, 255), 6)
        # draw rectangle on images having barcode area
        pos2 = barcode.rect
        # show the outcome or output of decoding
        cv2.putText(
            frames,
            output,
            (pos2[0], pos2[1]),
            cv2.FONT_HERSHEY_PLAIN,
            2,
            (0, 255, 0),
            2,
        )
    # show images/frames on scanner window
    cv2.imshow("scaner", frames)
    # funnctionality to clear and exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cap.release()
        break
