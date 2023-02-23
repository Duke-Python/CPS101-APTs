"""
Created on Sep 17, 2014

@author: George S. Hugh
"""


def bagelCount(orders):

    return sum([order + order//12 for order in orders])
