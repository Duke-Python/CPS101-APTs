
def list_of_children(person, parents, children):
    retval = []
    for parent, child in zip(parents, children):
        if parent == person:
            retval.append(child)
    return retval


def grandchildren(parents, children, person):
    """
    parents (list of strings) - list of parent names corresponding to the
          children list
    children (list of strings) - list of child names corresponding to the
          parents list
    person (string) - a person listed in parents
          
    Return the number of grandchildren for the person in the person variable
    """
    kids = list_of_children(person, parents, children)
    grandkids = 0
    for kid in kids:
        grandkids += len(list_of_children(kid, parents, children))

    return grandkids
