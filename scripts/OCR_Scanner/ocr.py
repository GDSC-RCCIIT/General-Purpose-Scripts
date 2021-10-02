from PIL import Image
import pytesseract
import numpy as np
# Incase If this link don't work try giving address path on your local machine while running the script
filename = 'https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/blob/main/scripts/OCR_Scanner/image_01.png'
img = np.array(Image.open(filename))
text = pytesseract.image_to_string(img)
# print(text)
content = text
with open("https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/blob/main/scripts/OCR_Scanner/ocr.txt","w") as f:
   content = f.write(content)
   f.close()
   
