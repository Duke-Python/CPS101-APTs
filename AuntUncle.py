"""
Created on Apr 9, 2012

@author: George S. Hugh
"""


# noinspection SpellCheckingInspection
def aulist(parents, target):

    par1 = ""
    par2 = ""
    family = {}
    for line in parents:
        parent1, parent2, kid = line.split()
        if kid == target:
            par1 = parent1
            par2 = parent2

        cur_par = parent1
        if cur_par in family:
            cur_kids = tuple(family[cur_par])
            cur_kids = cur_kids + (kid,)
        else:
            cur_kids = (kid,)
        family[cur_par] = cur_kids

        cur_par = parent2
        if cur_par in family:
            cur_kids = tuple(family[cur_par])
            cur_kids = cur_kids + (kid,)
        else:
            cur_kids = (kid,)
        family[cur_par] = cur_kids

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
