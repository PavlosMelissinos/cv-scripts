import numpy as np
import cv2
import sys
import os
from os.path import splitext, basename, join

VIDEO_FILE = sys.argv[1]
if len(sys.argv) > 2:
  FRAME_DIR = sys.argv[2]
else:
  directory = splitext(basename(VIDEO_FILE))[0]
  FRAME_DIR = 'data/{}'.format(directory)

try:
    os.stat(FRAME_DIR)
except:
    os.mkdir(FRAME_DIR)       

cap = cv2.VideoCapture(VIDEO_FILE)

if not cap.isOpened(): 
    print "could not open :",fn
    exit()

length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.cv.CV_CAP_PROP_FPS)

print 'Video length:', length
print 'Frame width:', width
print 'Frame height:', height
print 'Video fps:', fps

success,image = cap.read()
count = 0
success = True
while success:
  success,image = cap.read()
  filename = 'frame{}.jpg'.format(count)
  filepath = join(OUT_DIR, filename)
  print 'Read a new frame: ', success
  cv2.imwrite(filepath, image)     # save frame as JPEG file
  count += 1

cap.release()
cv2.destroyAllWindows()
