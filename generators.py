def chain(itt_one, itt_two):
    return (x for x in itt_one + itt_two)


def compress(itt, mask):
    return (itt[i] for i in range(len(mask))if mask[i] is True)


def cycle(itt):
    while True:
        return chain(itt, itt)
