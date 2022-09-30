"""
Created on Jan 30, 2012

@author: George S. Hugh
"""


def ratio(dna):
    """ return double that's the cg ratio 
    of the nucleotides in the string parameter dna
    """ 
    
    count = 0
    for acid in dna:
        if (acid == 'c') or (acid == 'g'):
            count = count + 1
            
    print(count)
            
#    [count++ for i in dna if ((i=='c') or (i=='g'))]

    return float(count) / len(dna)
