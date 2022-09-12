'''
Created on Nov 8, 2012

@author: hughgs
'''

from operator import itemgetter

def winners(data):

    name_list = [];
    task_list = [];
    time_list = [];
    for contestants in data:
        [name, time] = contestants.split(" ")
        if (name not in name_list):
            name_list.append(name)
        ind = name_list.index(name)
        if (len(task_list) <= ind):
            task_list.append(1)
            time_list.append(0)
        else:
            task_list[ind] = task_list[ind] + 1
        [minutes, sec] = time.split(":")
        time_list[ind] = time_list[ind] + \
                        (60*int(minutes) + int(sec))
                        
    print name_list
    print time_list

    tuple_list = [];
    for ind, name in enumerate(name_list):
        word_tuple = (name, task_list[ind], time_list[ind])
        tuple_list.append(word_tuple);

    tuple_list.sort(key=itemgetter(2))
    tuple_list.sort(key=itemgetter(1), reverse=True)

    return([i[0] for i in tuple_list])