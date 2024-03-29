"""
Created on Sep 10, 2014

@author: George S. Hugh
"""


def modify(name):
    
    names = name.split()
    list_length = len(names)

    if list_length == 1:
        return names[0]
    if list_length == 2:
        return names[1] + ", " + names[0]

    ret_str = names[-1] + ", " + names[0] + " "
    for middle_name in names[1:-1]:
        ret_str += middle_name[0]
        if len(middle_name) > 1:
            ret_str += "."
        ret_str += " "

    return ret_str[0:-1]
