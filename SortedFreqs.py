"""
Created on 4/4/2023

@author: George Hugh
"""


def freqs(data):
    name_dict = {}
    for name in data:
        if name not in name_dict:
            name_dict[name] = 0
        name_dict[name] += 1

    key_list = list(name_dict.keys())
    key_list.sort()

    ret_list = []
    for name in key_list:
        ret_list.append(name_dict[name])

    return ret_list
