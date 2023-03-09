"""
Created on 3/8/2023

@author: George Hugh
"""


def decrypt(library, message):
    """
    return String for parameters
    library a list of Strings
    and message a string
    """

    code_dict = {}
    for decoding in library:
        decode_list = decoding.split(" ")
        code_dict[decode_list[1]] = decode_list[0]

    decode = ""
    for encoding in message.split(" "):
        if encoding not in code_dict:
            decode += "?"
        else:
            decode += code_dict[encoding]

    return decode
