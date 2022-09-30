"""
Created on Feb 27, 2015

@author: George S. Hugh
"""


def calculate(weight, height):
    """ 
    return float indicating BMI (body mass index)
    given weight in pounds (float)
    given height in inches (float)
    """
    # you write code here
    
    bmi = 703.0695 * weight/(height*height)
    return bmi
