
def networth(transactions):
    """
    return list of strings based on transactions,
    which is also a list of strings
    """
    amt_dict = dict()
    for transaction in transactions:
        sender, receiver, amt_str = transaction.split(":")
        amt = int(100*float(amt_str))
        if sender not in amt_dict:
            amt_dict[sender] = 0
        if receiver not in amt_dict:
            amt_dict[receiver] = 0
        amt_dict[sender] -= amt
        amt_dict[receiver] += amt

    payers = [name + ":" + str(amt/100) for name, amt in amt_dict.items()]

    return sorted(payers)
