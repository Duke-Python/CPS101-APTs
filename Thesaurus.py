'''
Created on Dec 3, 2014

@author: hughgs
'''

def check(entries):

    numEntries = len(entries)
    combined = False

    i = 0
    j = 0
    while ((i < (numEntries-1)) and (not combined)):
        j = i + 1
        while ((j < numEntries) and (not combined)):
            combined = ((len(set(entries[i]) & set(entries[j]))) > 1)
            j = j + 1
        i = i + 1

    if combined:
        i = i - 1
        j = j - 1
                
    return(combined, i, j)

def join(entries, first, second):

    added = False
    retval = []
    numEntries = len(entries)
    for i in range(numEntries):
        if (i != first) and (i != second):
            retval.append(entries[i])
        elif (not added):
            retval.append(sorted(list(set(entries[first]) | set(entries[second]))))
            added = True

    return(retval)

def pretty(lists):
    
    retval = []
    for item in lists:
        retval.append(' '.join(item))
        
    return(retval)

def edit(entry):
    
    print "============================"

    entries = []
    for item in entry:
        entries.append(sorted(item.split()))

    [combined, i, j] = check(entries)
    while combined:
        entries = join(entries, i, j)
        combined, i, j = check(entries)

    return(sorted(pretty(entries)))
    
if __name__ == '__main__':

    test = ["ape monkey wrench", "wrench twist strain", "monkey twist frugue strain"]
    edit(test)
