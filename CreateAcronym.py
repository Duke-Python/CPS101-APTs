"""
Created on 2/22/2023

@author: George Hugh
"""


def acronym(phrase):
    """
    phrase is a string, zero or more spaces
    return a string: acronym of the string
    parameter phrase
    """

    return ''.join([word[0] for word in phrase.split(" ")])
