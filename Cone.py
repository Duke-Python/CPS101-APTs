"""
Created on 9/12/2022

@author: George Hugh
"""


def volume(radius, height):
    """
    return volume of a cone in cubic inches
    given float parameters radius and height in inches
    """

    pi  = 3.1415926
    cone_vol = 1.0/3.0  * pi * radius * radius * height
    return cone_vol


if __name__ == '__main__':
    pass
