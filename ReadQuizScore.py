"""
Created on 9/25/2022

@author: George Hugh
"""


def grade(total, availablePoints, cutOff):
    """
    return a student's reading quiz grade as a float percentage based on
    the integer values in total, availablePoints, and cutOff.
    """
    percent = total/(availablePoints*cutOff/100)*100
    if percent >= 100.0:
        return 100.0
    return percent


if __name__ == '__main__':
    pass
