def count(a, b):
    """
    return the integer number of characters in common
    to Strings a and b as described below
    """
    list_a = list(a)
    list_b = list(b)
    count = 0
    for letter in list_a:
        if letter in list_b:
            count += 1
            list_b.remove(letter)
    return count
