import os
from PIL import Image
from PIL.ExifTags import TAGS


img_path = input("Enter : Path of the image\n>> ")
Path_Exist = os.path.isfile(img_path)

image_file = img_path

try:
    image = Image.open(image_file)
except IOError:
    pass
exif = {}

f = open("metadata.txt", "w")

for tag, value in image._getexif().items():

    if tag in TAGS:
        exif[TAGS[tag]] = value
try:
    if "Copyright" in exif:
        print("Image is Copyrighted, by ", exif["Copyright"])
except KeyError:
    pass
print()
print("Printing all the metadatas of the image in metadata.txt : \n")
for key, value in exif.items():
    f.write("%s:%s\n" % (key, value))
