'''
Created on Sep 17, 2014

@author: hughgs
'''

def bagelCount(orders):

    count = 0
    for order in orders:
        count = count + order + order/12
        
    return(count)