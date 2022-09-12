'''
Created on Sep 27, 2012

@author: hughgs
'''
def whichOrder(available, orders):

    index = -1
    ret_val = -1
    for sandwiches in orders:

        barHas = True
        for ingredients in sandwiches.split(" "):
            barHas = barHas and (ingredients in available);

        if barHas and (ret_val == -1):
            ret_val = index + 1
        else:
            index = index + 1

    return(ret_val)