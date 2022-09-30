"""
Created on Sep 10, 2014

@author: George S. Hugh
"""


def modify(name):
    
    names = name.split()
    listLength = len(names)

    if listLength < 2:
        return names[0]
    if listLength == 2:
        return names[1] + ", " + names[0]

    retStr = names[-1] + ", " + names[0]
    for name in names[1:-1]:
        retStr = retStr + " " + name[0]
        if len(name) > 1:
            retStr = retStr + "."
    return retStr
