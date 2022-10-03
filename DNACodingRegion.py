"""
Created on Oct 28, 2014

@author: George S. Hugh
"""


def findRegion(dna):

    print("=============================")
    print(dna)
    retval = ""
    start_codon = "atg"
    stop_codons = ['taa', 'tag', 'tga']
    val1 = dna.find(start_codon)
    if start_codon not in dna:
        return retval

    for i in range(len(dna)):
        if dna[val1+i:val1+i+3] in stop_codons:
            if (len(dna[val1:val1+i+3]) % 3) == 0:
                retval += dna[val1+3:val1+i]
                return retval
    
    return retval
