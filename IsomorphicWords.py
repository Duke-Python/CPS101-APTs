"""
Created on Nov 29, 2012

@author: George S. Hugh
"""


def countPairs(words):
    
    count = 0
    baselist = words[:len(words)-1]
    for i, baseword in enumerate(baselist):

        testlist = words[i+1:len(words)]
        for testword in testlist:

            a2bMap = {}
            b2aMap = {}
            for k, bchar in enumerate(baseword):
                tchar = testword[k]
                a2bMap[bchar] = tchar
                b2aMap[tchar] = bchar
                
            wrdChecka = ""
            wrdCheckb = ""
            for k, bchar in enumerate(baseword):
                tchar = testword[k]
                wrdChecka = wrdChecka + a2bMap[bchar]
                wrdCheckb = wrdCheckb + b2aMap[tchar]

            if (wrdChecka == testword) and (wrdCheckb == baseword):
                count = count + 1
                
    return count
