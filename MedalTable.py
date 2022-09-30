"""
Created on Mar 26, 2012

@author: George S. Hugh
"""
from operator import itemgetter


def generate(results):

    medal_dict = {}
    for countries in results:
        medals = countries.split()
        for i, country in enumerate(medals):
            if country not in medal_dict:
                medal_count = [0, 0, 0]
            else:
                medal_count = medal_dict[country]
            medal_count[i] = medal_count[i] + 1
            medal_dict[country] = medal_count
    
    tuple_list = []
    for country in medal_dict:
        medal_count = medal_dict[country]
        medal_tuple = (country, medal_count[0], medal_count[1], medal_count[2])
        tuple_list.append(medal_tuple)
        
    tuple_list.sort(key=itemgetter(0))
    tuple_list.sort(key=itemgetter(1, 2, 3), reverse=True)

    return [medal_tuple[0] + " " + str(medal_tuple[1]) +
                             " " + str(medal_tuple[2]) +
                             " " + str(medal_tuple[3]) for medal_tuple in tuple_list]
