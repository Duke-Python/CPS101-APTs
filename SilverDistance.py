'''
Created on Sep 24, 2014

@author: hughgs
'''

def minSteps (sx, sy, gx, gy):

    if abs(gy-sy)>abs(gx-sx): # where it needs to go on y axis is greater than where it needs to go on x axis
        if (gy-sy)>0:         #if difference in y axis positive (needs to move up)
            return gy-sy
        if (gy-sy)<0:         #if difference in y axis negative (needs to move down)
            if abs((gy-sy)+abs(gx-sx))%2==0: #if difference of where it needs to go and where it is, is even
                return abs(gy-sy)
            else:
                return abs(gy-sy)+2
    else:                     # if where it needs to go on x axis is greater than where it needs to go on y axis
        if abs((gy-sy)+(gx-sx))%2==0:
            return abs(gx-sx)
        else:
            return abs(gx-sx)+1
