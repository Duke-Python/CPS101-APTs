"""
Created on 2/9/2023

@author: George Hugh
"""


def minutesNeeded(m):
    """
    Return integer number of minutes to launder m (integer) loads
    W -> D -> F
    1
    2    1
    3    2    1
    4    3    2
         4    3
              4
    """

    return m*25 + 35
