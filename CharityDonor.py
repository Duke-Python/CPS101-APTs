"""
Created on Nov 6, 2014

@author: George S. Hugh
"""


def nameDonor(contributions):
    
    print('========================')
    print(contributions)
    
    donor_map = dict()
    for contribution in contributions:
        temp = contribution.split(':')
        donor = temp[0]
        amt = float(temp[1])
            
        if donor in donor_map:
            total = donor_map.get(donor) + amt
            donor_map[donor] = total
        else:
            print([donor])
            donor_map[donor] = amt

    max_amt = max(donor_map.values())

    donor_list = []
    for donor in donor_map:
        if donor_map[donor] == max_amt:
            donor_list.append(donor)

    donor_list.sort()
    return donor_list[0]
        