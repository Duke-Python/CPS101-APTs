"""
Created on Sep 10, 2014

@author: George S. Hugh
"""


def modify(name):
    
    names = name.split()
    list_length = len(names)

    if list_length < 2:
        return names[0]
    if list_length == 2:
        return names[1] + ", " + names[0]

    ret_str = names[-1] + ", " + names[0]
    for name in names[1:-1]:
        ret_str = ret_str + " " + name[0]
        if len(name) > 1:
            ret_str = ret_str + "."
    return ret_str
