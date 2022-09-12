'''
Created on Oct 7, 2014

@author: hughgs
'''

def theMin(room):

    if (len(room) == 1):
        return(0)

    roomList = list(room)
    retval = 0
    switched = False
    colors = 'RGBY'
 
# Check all triples in the list

    for i in range(1,len(roomList)-1):
        matched = ((roomList[i] == roomList[i-1]) and (roomList[i] == roomList[i+1]))
        j = 0
        while (matched):
            switched = True
            roomList[i] = colors[j]
            j = j + 1
            matched = ((roomList[i] == roomList[i-1]) and (roomList[i] == roomList[i+1]))
        if (switched):
            retval = retval + 1
            switched = False

#   Check for single swaps
    
    for i in range(1,len(roomList)-1,2):
        matched = ((roomList[i] == roomList[i-1]) or (roomList[i] == roomList[i+1]))
        j = 0
        while (matched):
            switched = True
            roomList[i] = colors[j]
            j = j + 1
            matched = ((roomList[i] == roomList[i-1]) or (roomList[i] == roomList[i+1]))
        if (switched):
            retval = retval + 1
            switched = False

#   Check the last character

    i = len(roomList) - 1    
    matched = (roomList[i] == roomList[i-1])
    j = 0
    while (matched):
        switched = True
        roomList[i] = colors[j]
        j = j + 1
        matched = (roomList[i] == roomList[i-1])
         
    if (switched):
        retval = retval + 1
        
    return(retval)