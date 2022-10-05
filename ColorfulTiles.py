"""
Created on Oct 7, 2014

@author: George S. Hugh
"""


def theMin(room):

    if len(room) == 1:
        return 0

    room_list = list(room)
    retval = 0
    switched = False
    colors = ["R", "G", "B", "Y"]
 
# Check all triples in the list

    for i in range(1, len(room_list)-1):
        matched = ((room_list[i] == room_list[i-1]) and (room_list[i] == room_list[i+1]))
        j = 0
        while matched:
            switched = True
            room_list[i] = colors[j]
            j = j + 1
            matched = ((room_list[i] == room_list[i-1]) and (room_list[i] == room_list[i+1]))
        if switched:
            retval = retval + 1
            switched = False

#   Check for single swaps
    
    for i in range(1, len(room_list)-1, 2):
        matched = ((room_list[i] == room_list[i-1]) or (room_list[i] == room_list[i+1]))
        j = 0
        while matched:
            switched = True
            room_list[i] = colors[j]
            j = j + 1
            matched = ((room_list[i] == room_list[i-1]) or (room_list[i] == room_list[i+1]))
        if switched:
            retval = retval + 1
            switched = False

#   Check the last character

    i = len(room_list) - 1
    matched = (room_list[i] == room_list[i-1])
    j = 0
    while matched:
        switched = True
        room_list[i] = colors[j]
        j = j + 1
        matched = (room_list[i] == room_list[i-1])
         
    if switched:
        retval = retval + 1
        
    return retval
