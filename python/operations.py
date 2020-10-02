from typing import Union


def increment_by_n(n: Union[int, float]):
    """Generates a function that
    will increment by n.

    Args:
        n (int): integer to increment by.

    >>> increment_by_n(2)(2)
    4
    """

    def incrementor(base: Union[int, float]):
        return base + n

    return incrementor


def decrement_by_n(n: Union[int, float]):
    """Generates a function that
    will decrement by n.

    Args:
        n (int): integer to decrement
        by.

    >>> decrement_by_n(2)(2)
    0
    """

    def decrementor(base: Union[int, float]):
        return base - n

    return decrementor
