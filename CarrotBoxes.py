"""
Created on Oct 7, 2014

@author: George S. Hugh
"""


def theIndex(carrots, amount):
    """ carrots is a list of integers representing boxes of carrots,
    amount is int value. return int that is the index/box number
    of the box from which the last of amount carrots are eaten """

    box = None
    for _ in range(amount):
        box = carrots.index(max(carrots))
        carrots[box] -= 1
        
    return box
