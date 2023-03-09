"""
Created on Nov 3, 2015

@author: George S. Hugh
"""


def word_split(word, splitter):
    """
    Need to remove empty strings from list after split
    """
    split_list = word.split(splitter)
    return [item for item in split_list if len(item) != 0]


def check(word):
    """ Replace syllables with spaces, then remove spaces """

    syllables = ["pi", "ka", "chu"]
    new_word = word
    for syllable in syllables:
        new_word = new_word.replace(syllable, " ")
    new_word = new_word.replace(" ", "")

    if len(new_word) == 0:
        return "YES"
    return "NO"
