from random import randint
import numpy as np

def draw_bbox(canvas, bb):
    Bbox = namedtuple('Bbox', ['u','d','l','r'])
    bb = [int(b) for b in bb]
    xy = Bbox(u=bb[1], d=bb[1] + bb[3], l=bb[0], r=bb[0] + bb[2])
    fill_color = [random() for _ in range(3)]
    fill_color = [int(fc / max(fill_color) * 255) for fc in fill_color]
    canvas[xy.u, xy.l:xy.r] = fill_color  # upper horizontal
    canvas[xy.u:xy.d, xy.l] = fill_color  # left vertical
    canvas[xy.d, xy.l:xy.r] = fill_color  # lower horizontal
    canvas[xy.u:xy.d, xy.r] = fill_color  # right vertical
    return canvas
