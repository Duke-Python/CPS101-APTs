"""
Created on Sep 24, 2014

@author: George S. Hugh
"""


def minSteps(sx, sy, gx, gy):

    if abs(gy-sy) > abs(gx-sx):  # if desired y-axis position > desired x-axis position
        if (gy-sy) > 0:         # if difference in y-axis positive (needs to move up)
            return gy-sy
        if (gy-sy) < 0:         # if difference in y-axis negative (needs to move down)
            if abs((gy-sy)+abs(gx-sx)) % 2 == 0:  # if desired - current position is even
                return abs(gy-sy)
            else:
                return abs(gy-sy)+2
    if abs((gy-sy)+(gx-sx)) % 2 == 0:
        return abs(gx-sx)

    return abs(gx-sx)+1
