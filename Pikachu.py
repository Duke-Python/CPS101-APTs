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
    """ return String based on parameter word, a String """

    # pikachu = ["pi", "ka", "chu"]
    split_pi = word_split(word, "pi")
    for item in split_pi:
        split_ka = word_split(item, "ka")
        for item2 in split_ka:
            split_chu = word_split(item2, "chu")
            if len(split_chu) != 0:
                return "NO"
    return "YES"
