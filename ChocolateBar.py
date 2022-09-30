"""
Created on Oct 22, 2014

@author: George S. Hugh
"""


def uniqueLetters(str1):
    return len(set(str1)) == len(str1)


def maxLength(letters):
    
    if uniqueLetters(letters):
        return len(letters)

    maximum = 0
    for i in range(len(letters)):
        teststr = letters[i:]
        N = len(teststr)
        for j in range(N):
            teststr1 = teststr[0:N-j]
            if uniqueLetters(teststr1) and (len(teststr1) > maximum):
                maximum = len(teststr1)

    return maximum
                