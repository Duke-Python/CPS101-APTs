'''
Created on Sep 23, 2014

@author: hughgs
'''

def coins(pence):
    
    lbs = pence/240
    
    pence = pence - lbs*240
    shills = pence/12
    
    pennies = pence - shills*12
    if (pennies < 0):
        pennies = 0
    
    return( [lbs, shills, pennies] )