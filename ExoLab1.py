def diff(x, y):
    """ Calling function diff with arguments """


def my_map(func, arg1, arg2):
    """
    This will map the function 'func' to each pair
    of arguments in the list 'arg1' and 'arg2', returning
    the result
    """

    res = []

    for i, j in zip(arg1, arg2):
        res.append(func(i, j))

    return res

