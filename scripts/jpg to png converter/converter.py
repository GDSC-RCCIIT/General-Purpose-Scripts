import os
from PIL import Image


def converter():
  folderPath = 'D:\\crush\\'
  fileSequence = 1
  for filename in os.listdir(folderPath):
    im1 = Image.open(folderPath+filename)
    im1.save(f'D:\crush\png\{fileSequence}.png')
    fileSequence += 1

if __name__ == "__main__":
    converter()
