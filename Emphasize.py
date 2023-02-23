"""
Created on 2/22/2023

@author: George Hugh
"""


def repeat(word, number):
    """
    return the word with the first part of it repeated
    if it is a valid part to repeat. The part to be
    repeated must be repeated "number" times.
    If the first letter is not a vowel, and the third
    letter is a vowel, then the part to repeat is the
    first three letters.
    If the first and third letters are not vowels, but
    the second letter is, then the part to repeat is
    the first two letters.
    Otherwise, there is nothing to repeat.
    Only the first letter of the returned word may be
    a capital letter, if the original word started with
    a capital letter.
    """

    vowels = "aeiou"
    if word[0].lower() in vowels:
        return word

    if string_not_in(word[0:3], vowels):
        return word

    if len(word) < 3:
        return concat_string(word, number)

    if word[2].lower() in vowels:
        return concat_string(word[0:3], number) + word[3:]

    if word[2] not in vowels and word[1] in vowels:
        return concat_string(word[0:2], number) + word[2:]


def concat_string(cat_str, number):
    repeat_str = cat_str
    for _ in range(number-1):
        repeat_str += cat_str.lower()
    return repeat_str

def string_not_in(test_str, vowels):
    for letter in test_str:
        if letter in vowels:
            return False
    return True
