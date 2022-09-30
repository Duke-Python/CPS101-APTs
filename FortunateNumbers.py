"""
Created on Oct 15, 2014

@author: George S. Hugh
"""


def getFortunate(a, b, c):
    
    retval = set()
    fort_num = {'5', '8'}

    for ai in a:
        for bj in b:
            for ck in c:

                test_str = str(ai + bj + ck)   # possible number
                test_set = set(test_str) | fort_num   # add fortunate numbers to set

                if len(test_set) == len(fort_num):
                    retval.add(test_str)
                    
    return len(retval)
