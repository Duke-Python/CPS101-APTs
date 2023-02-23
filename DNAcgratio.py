"""
Created on Jan 30, 2012

@author: George S. Hugh
"""


def ratio(dna):
    """ return double that's the cg ratio 
    of the nucleotides in the string parameter dna
    """ 
    
    acid_list = [1 for i in dna if ((i=='c') or (i=='g'))]
    return len(acid_list)/len(dna)
