'''
Created on Apr 18, 2012

@author: hughgs
'''

def find(T,requiredTime):

    print "======================="    
    localtime = sorted(requiredTime)
    tasktime = localtime
    for i in range(1,len(localtime)):
        tasktime[i] = tasktime[i-1] + localtime[i]

    tasktime = [tasktime[i] for i in range(0,len(tasktime)) if tasktime[i] <= T]

    return([len(tasktime), sum(tasktime)])