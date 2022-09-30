"""
Created on Feb 23, 2012

@author: Hanna
"""


def encrypt(numbers):
    values = [numbers[n] for n in range(len(numbers))]
    product = 1
    for n in range(len(numbers)):
        product = product * numbers[n]
        new_product = [product/numbers[n] * (numbers[n] + 1) for n in range(len(numbers))]
    print("==========")
    print(numbers)
    print(values)
    print(product)
    print(new_product)
    print(max(new_product))
    integer = max(new_product)
    print(integer)
    return integer
