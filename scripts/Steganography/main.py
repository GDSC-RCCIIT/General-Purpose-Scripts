from LSBSteg import *
from voice import *
import voice
import os


print("--------------------------------------------------------------\n")
print(" ENCODING THE EMAIL AND PASSWORD TO THE IMAGE\n")
steg = LSBSteg(cv2.imread("my.jpg"))
txt = str(input(" Enter the text you want to encrypt : "))
img_encoded = steg.encode_text(txt)

cv2.imwrite("my_new_image.png", img_encoded)
print(
    "\n The size of the image before encryption : {} bytes".format(
        os.stat("my.jpg").st_size
    )
)


print("--------------------------------------------------------------\n")
print(" DECODING THE EMAIL AND PASSWORD FROM THE IMAGE\n")
im = cv2.imread("my_new_image.png")
steg = LSBSteg(im)
print(" Text value:", steg.decode_text())
print(
    "\n The size of the image after decryption : {} bytes".format(
        os.stat("my_new_image.png").st_size
    )
)

print("\n--------------------------------------------------------------\n")
