'''
Created on Feb 23, 2012

@author: Hann
'''
def encrypt(numbers):
    values = [numbers[n] for n in range(len(numbers))]
    product = 1
    for n in range(len(numbers)):
        product = long(product * numbers[n])
        new_product = [long(product/numbers[n] * (numbers[n] + 1)) for n in range(len(numbers))]
    print "=========="
    print numbers
    print values
    print product
    print new_product
    print long(max(new_product))
    integer = long(max(new_product))
    print integer
    return long(integer)