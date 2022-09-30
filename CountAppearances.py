"""
Created on Sep 17, 2014

@author: George S. Hugh
"""


def numberTimesAppear(number, digit):
    
    #     count = 0
    #     for i in str(number):
    #         if (i == str(digit)):
    #             count = count + 1

    count = sum(1 for i in str(number) if i == str(digit))
            
    return count
