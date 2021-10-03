from PIL import Image
import pytesseract
import numpy as np

# Input your Local Machine Address in filename where you have stored your image.
path = input("Enter your Image Path Address : ")
filename = path
try:
    img = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img)
    content = text
except:
    print("Invalid Image or Image path ! ")
# print(text)


# Input your Local Machine Address to open ocr.txt file
try:
    textfile = input("Enter the file path of text file : ")
    with open(
        textfile,
        "w",
    ) as f:
        content = f.write(content)
except:
    print("Invalid Path for text file !")
