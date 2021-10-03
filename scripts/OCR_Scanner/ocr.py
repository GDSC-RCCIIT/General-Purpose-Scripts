from PIL import Image
import pytesseract
import numpy as np

# Input your Local Machine Address in filename where you have stored your image.
path = input("Enter your Image Path Address : ")
filename = path
img = np.array(Image.open(filename))
text = pytesseract.image_to_string(img)
# print(text)
content = text

# Input your Local Machine Address to open ocr.txt file
textfile = input("Enter the file path of text file : ")
with open(
    textfile,
    "w",
) as f:
    content = f.write(content)
    f.close()
`
