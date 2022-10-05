"""
Created on Apr 9, 2012

@author: George S. Hugh
"""


def get_parents(parents, target):
    pass


def create_dictionary(parents):
    family = {}
    for line in parents:
        parent1, parent2, kid = line.split()
        family[kid] = [parent1, parent2]
    return family


# noinspection SpellCheckingInspection
def aulist(parents, target):

    family = create_dictionary(parents)
    aunt_unc = ()
    parents = family.keys()
    for cur_par in parents:
        if par1 in family[cur_par]:
            aunt_unc = aunt_unc + family[cur_par]
        if par2 in family[cur_par]:
            aunt_unc = aunt_unc + family[cur_par]

    aunt_unc = list(set(aunt_unc))
    if par1 in aunt_unc:
        aunt_unc.remove(par1)
    if par2 in aunt_unc:
        aunt_unc.remove(par2)
    if target in aunt_unc:
        aunt_unc.remove(target)

    return sorted(aunt_unc)
