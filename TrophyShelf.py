'''
Created on Oct 11, 2012

@author: hughgs
'''
def countVisible(trophies):
    
    left2right = 0
    max_height = 0
    for height in trophies:
        if (height > max_height):
            left2right = left2right+1
            max_height = height
            
    right2left = 0
    max_height = 0
    for height in reversed(trophies):
        if (height > max_height):
            right2left = right2left + 1
            max_height = height
    
    return([left2right, right2left])