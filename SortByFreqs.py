"""
Created on 4/12/2023

@author: George Hugh
"""


def sort(data):
    word_dict = dict()
    for word in data:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1

    tuple_list = [(word, count) for word, count in word_dict.items()]

    sorta = sorted(tuple_list, key=lambda x: x[0])
    sortb = sorted(sorta, key=lambda x: x[1], reverse=True)

    return [item[0] for item in sortb]
