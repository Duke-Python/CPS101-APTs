"""
Created on 4/24/2023

@author: George Hugh
"""


def sortinorder(phrase):
    """
    Given the string parameter phrase,
    which is a string of words, return the unique words
    from phrase sorted following the rules described. Return
    them as a string of words separated by a blank.
    """

    list1 = list(set(phrase.split(" ")))
    list1.sort(key=lambda x: x[1:-1])
    list1.sort(key=lambda x: x[-1], reverse=True)
    list1.sort(key=lambda x: x[0])
    list1.sort(key=len, reverse=True)

    return " ".join(list1)
