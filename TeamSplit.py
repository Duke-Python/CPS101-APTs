"""
Created on 4/24/2023

@author: George Hugh
"""


def difference(strengths):
    strengths.sort(reverse=True)
    team1 = sum(strengths[0::2])
    team2 = sum(strengths[1::2])

    return abs(team1 - team2)
