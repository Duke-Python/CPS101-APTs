'''
Created on Nov 8, 2012

@author: hughgs

Create list of tuples where each tuple has word and count, then sort

'''
from operator import itemgetter

def sort(data):
    
    tuple_list = [];
    for word in data:
        word_tuple = (word, data.count(word), len(word))
        if word_tuple not in tuple_list:
            tuple_list.append(word_tuple);

    tuple_list.sort(key=itemgetter(1,2,0))

    return([i[0] for i in tuple_list])