"""
Color.py
Author:  Michael Steer
Date:    2018-11-28
"""


class Color:

    def __init__(self, r=0, g=0, b=0, bulb=None) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.bulb = bulb

    def hsv(self) -> (int, int, int):
        rp = self.r / 255
        gp = self.g / 255
        bp = self.b / 255

        cmax = max(rp, gp, bp)
        cmin = min(rp, gp, bp)
        delta = cmax - cmin

        if delta == 0:
            h = 0
        elif cmax == rp:
            h = 60 * ((gp - bp) / delta) % 6
        elif cmax == gp:
            h = 60 * ((bp - rp) / delta) + 2
        else:
            h = 60 * ((rp - gp) / delta) + 4

        if cmax == 0:
            s = 0
        else:
            cmax = delta / cmax

        v = cmax

        return h, s, v

    def rgb(self):
        return self.r, self.g, self.b

    def get_bulb_value(self) -> int:
        pass


def hsv_to_rgb(h, s, v):
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        rp = c
        gp = x
        bp = 0
    elif 60 <= h < 120:
        rp = 0
        gp = c
        bp = 0
    elif 120 <= h < 180:
        rp = 0
        gp = c
        bp = x
    elif 180 <= h < 240:
        rp = 0
        gp = x
        bp = c
    elif 240 <= h < 300:
        rp = x
        gp = 0
        bp = c
    else:
        rp = c
        gp = 0
        bp = x

    r = (rp * m) * 255
    g = (gp * m) * 255
    b = (bp * m) * 255
    return r, g, b


BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
LIME = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
YELLOW = Color(255, 255, 0)
CYAN = Color(255, 0, 255)
SILVER = Color(192, 192, 192)
GRAY = Color(128, 128, 128)
MAROON = Color(128, 0, 0)
OLIVE = Color(128, 128, 0)
GREEN = Color(0, 128, 0)
PURPLE = Color(128, 0, 128)
TEAL = Color(0, 128, 128)
NAVY = Color(0, 0, 128)
