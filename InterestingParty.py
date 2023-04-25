"""
Created on 4/25/2023

@author: George Hugh
"""


def bestInvitation(first, second):
    """
    return int based on string list
    parameters first and second
    """
    topics = dict()
    for topic1, topic2 in zip(first, second):
        if topic1 not in topics:
            topics[topic1] = 0
        if topic2 not in topics:
            topics[topic2] = 0
        topics[topic1] += 1
        topics[topic2] += 1

    topic_list = list()
    for topic, count in topics.items():
        topic_list.append((topic, count))

    topic_list.sort(key=lambda x: x[1], reverse=True)

    return topic_list[0][1]
