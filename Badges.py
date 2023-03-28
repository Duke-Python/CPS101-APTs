def findLabel(labels, deeds, needs):
    """
    return string based on parameters
    labels a list of strings
    deeds a list of strings
    and needs a list of strings
    """
    accomplishment = set(deeds)
    for label, need in zip(labels, needs):
        if set(need.split(" ")).issubset(accomplishment):
            return label
    return "nobadge"
