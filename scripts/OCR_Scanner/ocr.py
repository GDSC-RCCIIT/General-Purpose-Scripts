from PIL import Image
import pytesseract
import numpy as np

filename = '/home/harshil/Desktop/image_01.png'
img = np.array(Image.open(filename))
text = pytesseract.image_to_string(img)
# print(text)
content = text
with open("/home/harshil/Documents/ocr.txt","w") as f:
   content = f.write(content)
   f.close()
   