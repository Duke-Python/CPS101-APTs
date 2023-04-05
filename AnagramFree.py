"""
Created on 4/4/2023

@author: George Hugh
"""


def not_anagram(word, anag_list):
    for anagram in anag_list:
        if is_anagram(word, anagram):
            return False
    return True


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    for ch in word1:
        word2 = word2.replace(ch, " ", 1)

    return len(word2.replace(" ", "")) == 0

    return len(word2) == 0


def getMaximumSubset(words):
    anagram_list = [words[0]]
    for word in words[1:]:
        if not_anagram(word, anagram_list):
            anagram_list.append(word)

    return len(anagram_list)


if __name__ == "__main__":
    word_list = ['abcd', 'abdc', 'dabc', 'bacd']
    print(getMaximumSubset(word_list))
