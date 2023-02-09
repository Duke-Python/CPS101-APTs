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

    words = [len(sentence.split()) for sentence in sentence_list]

    return sum(words)/len(sentence_list)
