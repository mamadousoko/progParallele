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
#print(result)

def calc_distance(point1, point2):
    """ Calling function calc_distance with arguments """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)**0.5


def my_map(func, arg1, arg2):
    """
    This will map the function 'func' to each pair
    of arguments in the list 'arg1' and 'arg2', returning
    the result
    """

    res = []

    for i, j in zip(arg1, arg2):
        res.append(func(i, j))

    return "{} \n {} \n and \n {}. \n {}".format(func.__doc__ , arg1, arg2, res)

points1 = [(1.0, 1.0, 1.0, 1.0, 1.0), (2.0, 2.0, 2.0, 2.0, 2.0), (3.0, 3.0, 3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0, 4.0, 4.0), (5.0, 5.0, 5.0, 5.0, 5.0), (6.0, 6.0, 6.0, 6.0, 6.0)]

distances = my_map(calc_distance, points1, points2)
print(distances)