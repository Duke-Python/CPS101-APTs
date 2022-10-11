"""
Created on Oct 28, 2014

@author: George S. Hugh
"""


def reversecomp(dna):

    dna_comp_dict = {"a": "t", "t": "a", "c": "g", "g": "c"}

    dna_comp = []
    for dna_part in dna:
        dna_comp.append(dna_comp_dict[dna_part])

    return dna_comp.reverse()
