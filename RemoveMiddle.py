"""
Created on Sep 10, 2014

@author: George S. Hugh
"""


def shorten(name):
    
    name_list = name.split()
    if len(name_list) > 1:
        return name_list[0] + " " + name_list[-1]
    return name_list[0]
