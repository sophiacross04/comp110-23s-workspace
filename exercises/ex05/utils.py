"""Ex05 - Utils."""

__author__: str = "730565129"


def only_evens(nums: list[int]) -> list[int]:
    """Returns only the evens from a list."""
    evens: list[int] = []  # empty list
    for idx in range(0, len(nums)):  # steps through every item in a list
        if nums[idx] % 2 == 0:
            evens.append(nums[idx])
    return evens


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Returns a list with the values from both lists in order."""
    both: list[int] = []  # empty list
    both = list1 + list2
    return both


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Creates a subset of a_list."""
    b_list: list[int] = []  # empty list

    # checking for errors with parameters
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if (len(a_list) == 0) or (start >= len(a_list)) or (end <= 0):
        return b_list

    # adds values from a_list to b_list if they are between start and end
    for idx in range(start, end):
        b_list.append(a_list[idx])
    return b_list