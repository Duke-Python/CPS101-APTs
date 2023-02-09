"""
Created on Feb 27, 2015

@author: George S. Hugh
"""


def weight3(ab, ac, bc):
    """
    (a + b) + (a + c) + (b + c) = ab + ac + bc
    2(a + b + c) = ab + ac + bc
    """
    
    return (ab+ac+bc)/2
