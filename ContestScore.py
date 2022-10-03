"""
Created on Apr 18, 2012

@author: George S. Hugh
"""


def find(t, required_time):

    print("=======================")
    localtime = sorted(required_time)
    task_time = localtime
    for i in range(1, len(localtime)):
        task_time[i] = task_time[i-1] + localtime[i]

    task_time = [task_time[i] for i in range(len(task_time)) if task_time[i] <= t]

    return [len(task_time), sum(task_time)]
