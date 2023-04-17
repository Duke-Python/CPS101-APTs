"""
Created on 4/12/2023

@author: George Hugh
"""


def minimumVotes(votes):
    if len(votes) == 1:
        return 0
    count = 0
    while votes[0] <= max(votes[1:]):
        count += 1
        cand = votes[1:].index(max(votes[1:])) + 1
        votes[0] += 1
        votes[cand] -= 1

    return count
