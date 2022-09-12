'''
Created on Oct 15, 2014

@author: hughgs
'''

def getFortunate(a, b, c):
    
    retval = set()
    fortNum = set(['5', '8'])

    for ai in a:
        for bj in b:
            for ck in c:

                testStr = str(ai + bj + ck)   # possible number
                testSet = set(testStr) | fortNum   # add fortunate numbers to set

                if (len(testSet) == len(fortNum)):
                    retval.add(testStr)
                    
    return(len(retval))
