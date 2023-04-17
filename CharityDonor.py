"""
Created on Nov 6, 2014

@author: George S. Hugh
"""


def nameDonor(contributions):
    
    donor_map = dict()
    for contribution in contributions:
        donor, amt = contribution.split(':')

        if donor not in donor_map:
            donor_map[donor] = 0
        donor_map[donor] += float(amt)*100

    max_amt = max(donor_map.values())

    donor_list = [donor for donor, amt in donor_map.items() if amt == max_amt]

    return sorted(donor_list)[0]
        