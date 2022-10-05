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


def wordScore(test_str, test_list1, test_list2):
    unique1 = wordNotInList(test_str, test_list1)
    unique2 = wordNotInList(test_str, test_list2)
    
    return calcScore(unique1, unique2)


def wordNotInList(test_str, test_list):
    return test_str not in test_list


def score(list_a, list_b, list_c):
    
    score_a = 0
    for word in list_a:
        score_a = score_a + wordScore(word, list_b, list_c)

    score_b = 0
    for word in list_b:
        score_b = score_b + wordScore(word, list_a, list_c)

    score_c = 0
    for word in list_c:
        score_c = score_c + wordScore(word, list_a, list_b)

    return str(score_a) + "/" + str(score_b) + "/" + str(score_c)
