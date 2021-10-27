#Import Libraries
import os
from PIL import Image

#Converter Function
def converter():
  folderPath = 'D:\\crush\\' #Location of the folder with jpg files
  fileSequence = 1
  for filename in os.listdir(folderPath):
    im1 = Image.open(folderPath+filename)
    im1.save(f'D:\crush\png\{fileSequence}.png') #Location of folder to save png files
    fileSequence += 1

if __name__ == "__main__":
    converter()
