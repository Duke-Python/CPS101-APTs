"""
Created on Oct 22, 2014

@author: George S. Hugh
"""


def calcScore(unique1, unique2):
    if unique1 and unique2:
        return 3
    if unique1 ^ unique2:
        return 2
    if (not unique1) and (not unique2):
        return 1
        
    return 0


def wordScore(testStr, testList1, testList2):
    unique1 = wordNotInList(testStr, testList1)
    unique2 = wordNotInList(testStr, testList2)
    
    return calcScore(unique1, unique2)


def wordNotInList(testStr, testList):
    return testStr not in testList


def score(listA, listB, listC):
    
    scoreA = 0
    for word in listA:
        scoreA = scoreA + wordScore(word, listB, listC)

    scoreB = 0
    for word in listB:
        scoreB = scoreB + wordScore(word, listA, listC)

    scoreC = 0
    for word in listC:
        scoreC = scoreC + wordScore(word, listA, listB)

    return str(scoreA) + "/" + str(scoreB) + "/" + str(scoreC)
