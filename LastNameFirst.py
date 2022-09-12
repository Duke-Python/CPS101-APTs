'''
Created on Sep 10, 2014

@author: hughgs
'''
def modify(name):
    
    names = name.split()
    listLength = len(names)
    
    if (listLength > 2):
        retStr = names[-1] + ", " + names[0]
        for name in names[1:-1]:
            retStr = retStr + " " + name[0]
            if (len(name) > 1):
                retStr = retStr + "."

    elif (listLength == 2):
        retStr = names[1] + ", " + names[0]

    else:
        retStr = names[0]

    return(retStr)