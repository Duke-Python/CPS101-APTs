'''
Created on Sep 17, 2014

@author: hughgs
'''

def lovely(ingredients, inedible):
    
    ingList = ingredients.split()
    blechyList = inedible.split()
    
    retval = 0
    for food in ingList:
        if (food not in blechyList):
            retval = retval + 1
            
    return(retval)