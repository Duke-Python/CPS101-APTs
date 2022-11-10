def findLabel(labels, deeds, needs):
    """
    return string based on parameters
    labels a list of strings
    deeds a list of strings
    and needs a list of strings
    """
    badges = {}
    for priority, (label, need) in enumerate(zip(labels, needs)):
        badges[label] = (priority, set(need.split(" ")))
    
    accomp = set(deeds)
    awards = [(21, "nobadge")]
    for label, (priority, needs) in badges.items():
        if needs.issubset(accomp):
            awards.append((priority, label))

#    awards.sort(key=lambda x: x[1])
    awards.sort()
    return awards[0][1]
