from PIL import Image
import os

files = [file for file in os.listdir() if file.endswith(".png")]

print(len(files))

for file in files:
    im = Image.open(file)
    #      x1   y1  x2   y2
    box = (323, 44, 944, 989)
    region = im.crop(box)
    region.save(file)

print("Done.")
