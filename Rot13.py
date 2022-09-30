"""
Created on Sep 27, 2012

@author: George S. Hugh
"""


def encrypt(original):
    origcode = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    newcode  = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"  # noqa

    ret_str = ""
    for letter in original:

        if letter not in origcode:
            ret_str = ret_str + letter
        else:
            ret_str = ret_str + newcode[origcode.find(letter)]

    return ret_str
