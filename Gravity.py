"""
Created on Feb 27, 2015

@author: George S. Hugh
"""


def falling(time, velo):
    
    g = 9.8
    d = velo*time + 0.5*g*time*time
    
    return d
