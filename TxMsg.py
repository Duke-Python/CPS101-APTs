"""
Created on Feb 1, 2012

@author: George S. Hugh
"""


def all_vowels(string):

    vowels = "aeiou"
    for letter in string:
        if letter not in vowels:
            return False
    return True


def make_cons(word):
    vowels = "aeiou"
    for vowel in vowels:
        word = word.replace(vowel, " ")
    return word.split(" ")


def getMessage(original):

    tx_msg = ""
#    print original

    words = original.split(" ")
    for word in original.split(" "):
        if not all_vowels(word):
            consonants = make_cons(word)
            tx_word = ""
            for sub in consonants:
                if sub != "":
                    tx_word += sub[0]
        else:
            tx_word = word

        tx_msg = tx_msg + " " + tx_word
        
    return tx_msg[1:]
