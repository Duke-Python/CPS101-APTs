"""
Created on 9/25/2022

@author: George Hugh
"""


def grade(total, available_points, cut_off):
    """
    return a student's reading quiz grade as a float percentage based on
    the integer values in total, availablePoints, and cutOff.
    """
    percent = total / (available_points * (cut_off/100)) * 100
    if percent >= 100.0:
        return 100.0
    return percent
