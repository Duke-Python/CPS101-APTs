"""
Created on Sep 17, 2014

@author: George S. Hugh
"""


def maxPoints(toss):
    counts = 6*[0]
    for die in toss:
        counts[die-1] += 1

    pts = []
    for multiplier in range(1, 7):
        pts.append(multiplier*counts[multiplier-1])

    return max(pts)
