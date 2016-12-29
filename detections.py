from collections import namedtuple
from random import randint
import numpy as np

def paint_bbox(canvas, bbox):
    Bbox = namedtuple('Bbox', ['u','d','l','r'])
    xy = Bbox(l=int(bb[1]), r=int(bb[1] + bb[3]), u=int(bb[0]), d=int(bb[0] + bb[2]))
    fill_color = [randint(100, 255), randint(100, 255), randint(100, 255)]
    print(fill_color)
    canvas[xy.l, xy.u:xy.d] = np.array(fill_color)  # connect upper left with upper right
    canvas[xy.l:xy.r, xy.u] = np.array(fill_color)
    canvas[xy.r, xy.u:xy.d] = np.array(fill_color)
    canvas[xy.l:xy.r, xy.d] = np.array(fill_color)
    return canvas
