"""
Created on Oct 28, 2014

@author: George S. Hugh
"""


def findRegion(dna):

    print("=============================")
    print(dna)
    retval = ""
    startCodon = "atg"
    stopCodons = ['taa', 'tag', 'tga']
    val1 = dna.find(startCodon)
    if startCodon not in dna:
        return retval

    for i in range(len(dna)):
        if dna[val1+i:val1+i+3] in stopCodons:
            if (len(dna[val1:val1+i+3]) % 3) == 0:
                retval += dna[val1+3:val1+i]
                return retval
    
    return retval
