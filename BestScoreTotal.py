"""
Created on 4/4/2023

@author: George Hugh
"""


def total(scores):
    result = 0
    for quiz_scores in scores:
        score_list = [int(score) for score in quiz_scores.split()]
        result += max(score_list)

    return result
