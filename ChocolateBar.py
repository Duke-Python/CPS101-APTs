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
        n = len(teststr)
        for j in range(n):
            teststr1 = teststr[:n-j]
            if uniqueLetters(teststr1) and (len(teststr1) > maximum):
                maximum = len(teststr1)

    return maximum
                