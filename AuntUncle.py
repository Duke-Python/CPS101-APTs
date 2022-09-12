'''
Created on Apr 9, 2012

@author: hughgs
'''

def aulist(parents,target):

    Par1 = ""
    Par2 = ""
    family = {}
    for line in parents:
        temp = line.split()
        parent1 = temp[0]
        parent2 = temp[1]
        kid = temp[2]
        if (kid == target):
            Par1 = parent1
            Par2 = parent2

        curPar = parent1
        if (curPar in family):
            curKids = tuple(family[curPar])
            curKids = curKids + (kid,)
        else:
            curKids = (kid,)
        family[curPar] = curKids

        curPar = parent2
        if (curPar in family):
            curKids = tuple(family[curPar])
            curKids = curKids + (kid,)
        else:
            curKids = (kid,)
        family[curPar] = curKids

    AuntUnc = ()
    parents = family.keys()
    for curPar in parents:
        if (Par1 in family[curPar]):
            AuntUnc = AuntUnc + family[curPar]
        if (Par2 in family[curPar]):
            AuntUnc = AuntUnc + family[curPar]

    AuntUnc = list(set(AuntUnc))
    if (Par1 in AuntUnc):
        AuntUnc.remove(Par1)
    if (Par2 in AuntUnc):
        AuntUnc.remove(Par2)
    if (target in AuntUnc):
        AuntUnc.remove(target)

    return(sorted(AuntUnc))
