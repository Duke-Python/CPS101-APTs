"""
Created on Mar 19, 2012

@author: George S. Hugh
"""


def highestScore(friends):

    print("========================")
    print(friends)

    max_friends = 0
    for k in range(len(friends)):
        line = friends[k]
        yeses = [i for i in range(len(line)) if line[i] == "Y"]
        yeses.append(k)
        print(yeses)
        for i in range(len(yeses)-1):
            temp = friends[yeses[i]]
            pos_friends = [j for j in range(len(temp)) if temp[j] == "Y"]
            print(str(i) + ": " + str(pos_friends))
            for j in range(len(pos_friends)):
                yeses.append(pos_friends[j])
            print(yeses)

        num_friends = len(set(yeses)) - 1
        if num_friends > max_friends:
            max_friends = num_friends

    return max_friends
