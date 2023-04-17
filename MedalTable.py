"""
Created on Mar 26, 2012

@author: George S. Hugh
"""


def generate(results):

    medal_dict = {}
    for countries in results:
        medals = countries.split()
        for i, country in enumerate(medals):
            if country not in medal_dict:
                medal_dict[country] = [0, 0, 0]
            medal_dict[country][i] += 1
    
    tuple_list = []
    for country, medal_count in medal_dict.items():
        tuple_list.append((country, medal_count))

    list_country = sorted(tuple_list)
    list_br = sorted(list_country, key=lambda x: x[1][2], reverse=True)
    list_sil = sorted(list_br, key=lambda x: x[1][1], reverse=True)
    list_gold = sorted(list_sil, key=lambda x: x[1][0], reverse=True)

    return [medal_tuple[0] + " " + " ".join([str(medal) for medal in medal_tuple[1]]) for medal_tuple in list_gold]
