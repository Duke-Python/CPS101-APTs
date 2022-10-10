"""
Created on Apr 9, 2012

@author: George S. Hugh
"""


def get_parents(parents, target):
    pass


def create_kid_dictionary(parents):
    """
    Create dictionary of kids with a list of parents
    """
    family = {}
    for line in parents:
        parent1, parent2, kid = line.split()
        family[kid] = [parent1, parent2]
    return family


def add_to_dict(dictionary, key, value):
    """
    Create dictionary of parents with a set of kids
    """
    if key in dictionary:
        dictionary[key] = dictionary[key].add(value)
    if key not in dictionary:
        dictionary[key] = set(value)


def create_par_dictionary(parents):
    family = {}
    for line in parents:
        parent1, parent2, kid = line.split()
        add_to_dict(family, parent1, kid)
        add_to_dict(family, parent2, kid)
    return family


# noinspection SpellCheckingInspection
def aulist(parents, target):

    kid_dict = create_kid_dictionary(parents)
    par_dict = create_par_dictionary(parents)
    par1, par2 = kid_dict[target]
    grands = kid_dict[par1]
    grands = grands + kid_dict[par2]
    aunt_unc = set()
    for cur_grand in grands:
        aunt_unc.add(par_dict[cur_grand])

    return sorted(aunt_unc)
