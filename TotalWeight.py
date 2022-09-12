'''
Created on Feb 27, 2015

@author: hughgs
'''
def weight3(ab,ac,bc):
    
    a = (ab + ac - bc)/2
    b = (ab + bc - ac)/2
    c = (ac + bc - ab)/2
    
    return(a+b+c)