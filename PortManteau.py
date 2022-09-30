"""
Created on 9/25/2022

@author: George Hugh
"""


def combine(first, flen, second, slen):
    """
    return string that's a portmanteau
    of strings first and second
    using flen chars from first
    and slen chars from second
    """

    return first[0:flen]+second[-slen:]


if __name__ == '__main__':
    pass
