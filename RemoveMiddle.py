'''
Created on Sep 10, 2014

@author: hughgs
'''
def shorten(name):
    
    nameList = name.split()
    listLength = len(nameList)
    
    if (listLength > 1):
        return(nameList[0] + " " + nameList[listLength-1])
    else:
        return(nameList[0])
