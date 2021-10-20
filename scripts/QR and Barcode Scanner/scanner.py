from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

# Image Path Or Image Name if in Same Directory or Replace the png file with your image

img_path = "frame.png"


def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    # Print results
    for obj in decodedObjects:
        print("Type : ", obj.type)
        s = str(obj.data)
        s = s.replace(s[0], "")
        s = s.replace("'", "")
        print("Data : ", s, "\n")

    return decodedObjects


# Display barcode and QR code location
def display(im, decodedObjects):

    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(
                np.array([point for point in points], dtype=np.float32)
            )
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points

        # Number of points in the convex hull
        n = len(hull)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    # Display results
    cv2.imshow("Results", im)
    cv2.waitKey(0)
    print("Done")


# Main
if __name__ == "__main__":

    # Read image
    im = cv2.imread(img_path)

    decodedObjects = decode(im)

    display(im, decodedObjects)
