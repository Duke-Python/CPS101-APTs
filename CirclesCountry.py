"""
Created on Oct 8, 2014

@author: George S. Hugh
"""


def leastBorders(x, y, r, x1, y1, x2, y2):

    start_cir = list()
    end_cir = list()
    for i in range(len(x)):
        xc = x[i]
        yc = y[i]
        rc = r[i]
        
        if ((x1-xc)**2 + (y1-yc)**2) < (rc**2):
            start_cir.append(i)
        
        if ((x2-xc)**2 + (y2-yc)**2) < (rc**2):
            end_cir.append(i)

    retval = len((set(start_cir) | set(end_cir))) - len((set(start_cir) & set(end_cir)))

    return retval
