from PIL import Image
import pytesseract
import numpy as np

#Input your Local Machine Address in filename where you have stored your image.
filename = 'https://github.com/Harshil-Jani/General-Purpose-Scripts/blob/OCR-Script/scripts/OCR_Scanner/image_01.png'
img = np.array(Image.open(filename))
text = pytesseract.image_to_string(img)
# print(text)
content = text

#Input your Local Machine Address to open ocr.txt file
with open("https://github.com/Harshil-Jani/General-Purpose-Scripts/blob/OCR-Script/scripts/OCR_Scanner/ocr.txt","w") as f:
   content = f.write(content)
   f.close()
   
