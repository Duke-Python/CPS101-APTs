'''
Created on Oct 15, 2014

@author: hughgs
'''

def howMany(meals, restaurant):
 
    retval = set()
    if (len(meals) > 0):
        for diner in meals:
            if restaurant in diner:
                retval.add(diner.split(":")[0])

    return(len(retval))
