# create a video by sequentially reading images from images/seq.jpg
import cv2
import os
import json

info = json.load(open("info.json", "r"))
print(info)
img_array = []
for i in range(1, len(info) + 1):
    filename = "images/{}.jpg".format(i)
    if os.path.isfile(filename):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)
    else:
        print("File {} not found".format(filename))

# mp4 format
out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15, size)
# output
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
