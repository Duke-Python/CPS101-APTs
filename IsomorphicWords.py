"""
Created on Nov 29, 2012

@author: George S. Hugh
"""


def countPairs(words):
    
    count = 0
    base_list = words[:len(words)-1]
    for i, base_word in enumerate(base_list):

        testlist = words[i+1:len(words)]
        for test_word in testlist:

            a2b_map = {}
            b2a_map = {}
            for k, bchar in enumerate(base_word):
                tchar = test_word[k]
                a2b_map[bchar] = tchar
                b2a_map[tchar] = bchar
                
            wrd_checka = ""
            wrd_checkb = ""
            for k, bchar in enumerate(base_word):
                tchar = test_word[k]
                wrd_checka = wrd_checka + a2b_map[bchar]
                wrd_checkb = wrd_checkb + b2a_map[tchar]

            if (wrd_checka == test_word) and (wrd_checkb == base_word):
                count = count + 1
                
    return count
