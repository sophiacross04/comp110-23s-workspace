"""Ex04 - list utility functions!"""

__author__: str = "730565129"


def all(list: list[int], inty: int) -> bool:
    """Checks to see if all of the values of the list are the same as the int."""
    # establishing variables
    x: bool = False
    i: int = 0

    # checks each index of the list
    while i < (len(list) - 1):
        if inty == list[i]:
            x = True
        else:
            x = False
            return x
        i += 1
    return x


def max(list: list[int]) -> int:
    """Returns the largest int from a list."""
    # raises error is the list is empty
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    
    # defining variables
    i: int = 0
    max: int = list[0]

    # checks each index of the list and updates when there is a larger number
    while i < (len(list) - 1):
        if max > list[i + 1]:
            max = max
        else:  # list[i + 1] > max
            max = list[i + 1]
        i += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if lists are deeply equal."""
    if list1 == list2:
        return True
    else:
        return False
