from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-pic", type=str)
args = parser.parse_args()

image = Image.open(args.pic)
image.save("compressed.jpg", quality=20, optimize=True)
