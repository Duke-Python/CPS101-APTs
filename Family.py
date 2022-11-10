def grandchildren(parents, children, person):
    """
    parents (list of strings) - list of parent names corresponding to the
          children list
    children (list of strings) - list of child names corresponding to the
          parents list
    person (string) - a person listed in parents
          
    Return the number of grandchildren for the person in the person variable
    """
    kids = {}
    for parent, kid in zip(parents, children):
        if parent in kids:
            kids[parent].append(kid)
        else:
            kids[parent] = [kid]

    grandkids = 0
    first_gen = kids[person]
    for parent in first_gen:
        if parent in kids:
            grandkids += len(kids[parent])

    return grandkids
