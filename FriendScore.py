"""
Created on Mar 19, 2012

@author: George S. Hugh
"""


def highestScore(friends):

    print("========================")
    print(friends)

    maxFriends = 0
    for k in range(len(friends)):
        line = friends[k]
        yeses = [i for i in range(len(line)) if line[i] == "Y"]
        yeses.append(k)
        print(yeses)
        for i in range(len(yeses)-1):
            temp = friends[yeses[i]]
            posFriends = [j for j in range(len(temp)) if temp[j] == "Y"]
            print(str(i) + ": " + str(posFriends))
            for j in range(len(posFriends)):
                yeses.append(posFriends[j])
            print(yeses)

        numFriends = len(set(yeses)) - 1
        if numFriends > maxFriends:
            maxFriends = numFriends

    return maxFriends
