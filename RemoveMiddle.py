"""
Created on Sep 10, 2014

@author: George S. Hugh
"""


def shorten(name):
    
    nameList = name.split()
    if len(nameList) > 1:
        return nameList[0] + " " + nameList[-1]
    return nameList[0]
