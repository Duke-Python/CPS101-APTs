"""
Created on Oct 15, 2014

@author: George S. Hugh
"""


def createSet(zoos, ind):
    
    retval = set()
    for i in range(len(zoos)):
        if i != ind:
            retval = retval.union(zoos[i].split(" "))
            
    return retval


def numberUnique(zoos):

    count = 0
    for i in range(len(zoos)):
        
        test_set = createSet(zoos, i)

        temp_set = test_set.union(zoos[i].split(" "))
        if len(test_set) != len(temp_set):
            count = count + 1
        
    return count
