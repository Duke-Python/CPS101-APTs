"""
Created on Feb 22, 2012

@author: George S. Hugh
"""


def whosDishonest(club1, club2, club3):
    
    cheat12 = set(club1).intersection(set(club2))
    cheat13 = set(club1).intersection(set(club3))
    cheat23 = set(club2).intersection(set(club3))
    
    print("================")
    print(cheat12)
    print(cheat13)
    print(cheat23)
    
    return list(cheat12)
