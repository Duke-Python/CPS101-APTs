"""
Created on Sep 27, 2012

@author: George S. Hugh
"""


def whichOrder(available, orders):

    index = -1
    ret_val = -1
    for sandwiches in orders:

        bar_has = True
        for ingredients in sandwiches.split(" "):
            bar_has = bar_has and (ingredients in available)

        if bar_has and (ret_val == -1):
            ret_val = index + 1
        else:
            index = index + 1

    return ret_val
