"""
Created on Sep 17, 2014

@author: George S. Hugh
"""


def lovely(ingredients, inedible):
    
    ing_list = ingredients.split()
    blechy_list = inedible.split()
    
    edible_list = [food for food in ing_list if food not in blechy_list]

    return len(edible_list)
