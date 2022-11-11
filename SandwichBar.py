"""
Created on Sep 27, 2012

@author: George S. Hugh
"""


def whichOrder(available, orders):

    avail_set = set(available)
    for index, sandwiches in enumerate(orders):
        ingredients = set(sandwiches.split(" "))
        if ingredients.issubset(avail_set):
            return index

    return -1
