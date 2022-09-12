'''
Created on Mar 19, 2012

@author: hughgs
'''

def highestScore(friends):

    print "========================"
    print friends

    maxFriends = 0
    for k in range(0,len(friends)):
        line = friends[k]
        yeses = [i for i in range(0,len(line)) if line[i]=="Y"]
        yeses.append(k)
        print yeses
        for i in range(0,len(yeses)-1):
            temp = friends[yeses[i]]
            posFriends = [j for j in range(0,len(temp)) if temp[j]=="Y"]
            print str(i) + ": " + str(posFriends)
            for j in range(0,len(posFriends)):
                yeses.append(posFriends[j])
            print yeses

        numFriends = len(set(yeses)) - 1
        if (numFriends > maxFriends):
            maxFriends = numFriends

    return(maxFriends)
