import numpy as np
import cv2
import sys
from os import listdir
from os.path import isfile, join

mypath = sys.argv[1]
videoname = sys.argv[2]
images = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[-3:]=='jpg']
images.sort()

# Define the codec and create VideoWriter object
fourcc = cv2.cv.FOURCC(*'XVID')
OUT_FILE = join(mypath, videoname)
out = None
print 'Saving to', OUT_FILE

W = 0
H = 0
for file in images:
    fullpath = join(mypath, file)
    frame = cv2.imread(fullpath)
    if W == 0 or H == 0:
        H = frame.shape[0]
        W = frame.shape[1]
        out = cv2.VideoWriter(OUT_FILE, fourcc, 2.5, (W, H))

    print frame.shape
    out.write(frame)

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

