"""
Created on 9/12/2022

@author: George Hugh
"""


def convert(r, g, b):
    """
    return float value obtained by
    converting integer r,g,b, into grayscale
    """

    grayscale = 0.21*r + 0.71*g + 0.07*b
    return grayscale


if __name__ == '__main__':
    pass
