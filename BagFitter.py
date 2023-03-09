"""
Created on 3/8/2023

@author: George Hugh
"""

import math


def bags(strength, food):
    """
    return int based on parameters strength, an int
    and food a list of Strings
    """

    food_dict = {}
    for item in food:
        if item not in food_dict.keys():
            food_dict[item] = 0
        food_dict[item] += 1

    bag_list = []
    for num_items in food_dict.values():
        bag_list.append(math.ceil(num_items/strength))

    return sum(bag_list)