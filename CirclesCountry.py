'''
Created on Oct 8, 2014

@author: hughgs
'''

def leastBorders(x,y,r,x1,y1,x2,y2):

    startCir = list();
    endCir = list();
    for i in range(len(x)):
        xc = x[i]
        yc = y[i]
        rc = r[i]
        
        if (((x1-xc)**2 + (y1-yc)**2) < (rc**2)):
            startCir.append(i)
        
        if (((x2-xc)**2 + (y2-yc)**2) < (rc**2)):
            endCir.append(i)

    retval = len((set(startCir) | set(endCir))) - len((set(startCir) & set(endCir)))

    return(retval)