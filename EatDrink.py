"""
Created on Nov 8, 2012

@author: George S. Hugh
"""


def winners(data):

    con_dict = dict()
    for contestants in data:
        [name, time] = contestants.split(" ")
        if name not in con_dict:
            con_dict[name] = (0, 0)
        [minutes, sec] = time.split(":")
        task_time = 60*int(minutes) + int(sec)
        new_tuple = (con_dict[name][0]+1, con_dict[name][1]+task_time)
        con_dict[name] = new_tuple

    tuple_list = []
    for name, task_and_time in con_dict.items():
        tuple_list.append((name, task_and_time[0], task_and_time[1]))

    tuple_list.sort(key=lambda x: x[2])
    tuple_list.sort(key=lambda x: x[1], reverse=True)

    return [item[0] for item in tuple_list]
