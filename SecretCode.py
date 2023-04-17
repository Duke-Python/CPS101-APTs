"""
Created on 4/12/2023

@author: George Hugh
"""


def decrypt(message, numbers):
    words = message.split(" ")
    code = ""
    for word, index in zip(words, numbers):
        if len(word) > index >= -len(word):
            code += word[index]

    return code
