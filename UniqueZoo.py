'''
Created on Oct 15, 2014

@author: hughgs
'''

def createSet(zoos, ind):
    
    retval = set()
    for i in range(len(zoos)):
        if (i != ind):
            retval = retval.union(zoos[i].split(" "))
            
    return(retval)

def numberUnique(zoos):

    count = 0
    for i in range(len(zoos)):
        
        testSet = createSet(zoos, i)

        tempSet = testSet.union(zoos[i].split(" "))
        if (len(testSet) != len(tempSet)):
            count = count + 1
        
    return(count)        