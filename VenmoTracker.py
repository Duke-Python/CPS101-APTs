
NAMES = []
CASH_FLOWS = []


def add_amt(name, amt):
    if name in NAMES:
        ind = NAMES.index(name)
        CASH_FLOWS[ind] += amt
    else:
        NAMES.append(name)
        CASH_FLOWS.append(amt)


def networth(transactions):
    """
    return list of strings based on transactions,
    which is also a list of strings
    """
    NAMES.clear()
    CASH_FLOWS.clear()
    for trans in transactions:
        sender, receiver, amt_str = trans.split(":")
        amt = int(100*float(amt_str))
        add_amt(sender, -amt)
        add_amt(receiver, amt)

    payers = [name + ":" + str(CASH_FLOWS[ind]/100)
              for ind, name in enumerate(NAMES)]
    print(payers)
    payers.sort()
    return payers
