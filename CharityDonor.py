'''
Created on Nov 6, 2014

@author: hughgs
'''
def nameDonor(contributions):
    
    print '========================'
    print contributions
    
    donorMap = dict()
    for contribution in contributions:
        temp = contribution.split(':')
        donor = temp[0]
        amt = float(temp[1])
            
        if donor in donorMap:
            total = donorMap.get(donor) + amt
            donorMap[donor] = total
        else:
            print [donor]
            donorMap[donor] = amt

    maxAmt = max(donorMap.values())

    donorList = []
    for donor in donorMap:
        if donorMap[donor] == maxAmt:
            donorList.append(donor)

    donorList.sort()
    return(donorList[0])
        
        