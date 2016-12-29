import cv2
import sys

jpg_in = sys.argv[1]
jpg_out = sys.argv[2]
width = float(sys.argv[3])

img = cv2.imread(jpg_in)

horig = float(img.shape[0])
worig = float(img.shape[1])

if width < 1:
  ratio = width
  wsize = int(ratio * worig)
  hsize = int(ratio * horig)
else:
  ratio = width / worig
  wsize = int(width)
  hsize = int(float(horig) * float(ratio))

img = cv2.resize(img, (wsize, hsize), interpolation=cv2.INTER_AREA)
cv2.imwrite(jpg_out, img)
