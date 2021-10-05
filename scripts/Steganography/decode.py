from LSBSteg import *

im = cv2.imread("my_new_image.png")
steg = LSBSteg(im)
print("Text value:", steg.decode_text())
print("Text value:", steg.decode_text())
