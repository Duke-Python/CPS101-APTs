'''
Created on Dec 9, 2014

Overall algorithm is wrong.  Probably need to include depth of tree.

@author: hughgs
'''

def getWeight(node, supervisors):
    
    children = [i for [i, child] in enumerate(supervisors) if child == node]
    print children
    numChildren = len(children)
    if numChildren == 0:
        return(0)
    else:
        temp = [getWeight(i, supervisors) for i in children]
        print "temp = ", temp
        weight = max(temp) + (numChildren - 1)
        print "   ", weight
        if all(temp[0] == item for item in temp):
            weight = weight + 1
        return(weight)

def minTime(supervisors):

    print "============================================"
    print supervisors
    
    return(getWeight(0, supervisors))
        
if __name__ == '__main__':

    test = [-1, 0, 0, 0, 3, 2, 5, 2, 4, 7]
    temp = minTime(test)
    
    print "Expected minimum time = 4"
    print "Actual minimum time = ", temp
