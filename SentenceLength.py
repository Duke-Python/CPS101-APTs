"""
Created on 9/25/2022

@author: George Hugh
"""


def average(sentenceList):
    """
    returns the average sentence length
    of all the sentences in sentenceList, a
    list of white-space delimited strings.
    """

    total_words = 0
    for sentence in sentenceList:
        total_words = total_words + len(sentence.split())

    return total_words/len(sentenceList)


if __name__ == '__main__':
    pass
