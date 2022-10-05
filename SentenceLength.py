"""
Created on 9/25/2022

@author: George S. Hugh
"""


def average(sentence_list):
    """
    returns the average sentence length
    of all the sentences in sentenceList, a
    list of white-space delimited strings.
    """

    total_words = 0
    for sentence in sentence_list:
        total_words = total_words + len(sentence.split())

    return total_words/len(sentence_list)
