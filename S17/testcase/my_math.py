def fact(n):
    """

    >>> fact(1)
    1
    >>> fact(0)
    1

    :param n:
    :return:
    """
    if not isinstance(n, int):
        raise TypeError

    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f


if __name__ == '__main__':
    import doctest
    doctest.testmod()