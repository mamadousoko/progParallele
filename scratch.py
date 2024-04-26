def diff(x, y):
    """ Calling function diff with arguments """
    return x - y

def my_map(func, arg1, arg2):
    """
    This will map the function 'func' to each pair
    of arguments in the list 'arg1' and 'arg2', returning
    the result
    """

    res = []

    for i, j in zip(arg1, arg2):
        res.append(func(i, j))

    return "{} {} and {}. \n {}".format(func.__doc__ , arg1, arg2, res)

a = [1,2,3,4,5]
b = [6,7,8,9,10]

result = my_map(diff, a, b)
print(result)
