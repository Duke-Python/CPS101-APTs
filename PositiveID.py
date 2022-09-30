"""
Created on Mar 26, 2012

@author: Hann
"""


def maximumFacts(suspects):
    print("+++++++++++")
    print(suspects)
#    print([suspects[0]]
    print({suspects[0]})
    a = {'a', 'b', 'c'}
    b = {'b', 'c', 'd'}
    print(a)
    print(b)
    c = a & b
    print(c)
    print(len(suspects))
    suspect_char = []
    for x in range(len(suspects)):
        # suspects.strip()
        # suspects.split(",")
        suspect_char.append([suspects[x]])
    print(suspects)
    print(suspect_char)
    max_len = 0
    for i in range(len(suspect_char)+1):
        for j in range(i+1, len(suspect_char)):
            print("====suspect_char[i]====")
            print(suspect_char[i])
            print("====suspect_char[j]====")
            print(suspect_char[j])
            set_i = set(suspect_char[i])
            set_j = set(suspect_char[j])
            print(set_i)
            print(set_j)
            not_common = set_i | set_j
            in_common = set_i & set_j
            print(not_common)
            print(in_common)
            char_len = len(in_common)
            if char_len > max_len:
                max_len = char_len

    return max_len
