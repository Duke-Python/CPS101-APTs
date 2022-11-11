def findLabel(labels, deeds, needs):
    """
    return string based on parameters
    labels a list of strings
    deeds a list of strings
    and needs a list of strings
    """
    accomp = set(deeds)
    for label, need in zip(labels, needs):
        if set(need.split(" ")).issubset(accomp):
            return label
    return "nobadge"
