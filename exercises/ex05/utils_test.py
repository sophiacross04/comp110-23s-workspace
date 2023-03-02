"""Testing utils.py!"""

__author__: str = "730565129"

from exercises.ex05.utils import only_evens, sub, concat

# Unit tests for only_evens


def test_evens_empty() -> None:
    """Edge case: tests if only_evens will return an empty list if an empty list is given."""
    assert only_evens([]) == []


def test_evens_mult() -> None:
    """Use case 1: tests if positive ints will add to the new list only if they are even."""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ([2, 4, 6, 8, 10])


def test_evens_negatives() -> None:
    """Use case 2: tests if negative ints will still add to the new list if they are even."""
    assert only_evens([-2, -3, -4, -5]) == [-2, -4]


# Unit tests for sub

def test_sub_empty() -> None:
    """Edge case: tests if sub will return an empty list if given an empty list."""
    assert sub([], 1, 4) == []


def test_sub_mult() -> None:
    """Use case 1: tests if sub will return a new list of values between the start and end parameters."""
    assert sub([1, 2, 3, 4, 5], 2, 4) == [3, 4]


def test_sub_wrong() -> None:
    """Use case 2: tests of sub will amend any errors with given start and end parameters."""
    assert sub([1, 2, 3, 4, 5], -1, 10) == [1, 2, 3, 4, 5]


# Unit tests for concat

def test_concat_empty() -> None:
    """Edge case: tests if concat will return an empty list if given two empty lists."""
    assert concat([], []) == []


def test_concat_mult() -> None:
    """Use case 1: tests if concat will return a concatenated list when given two lists."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_negatives() -> None:
    """Use case 2: tests if concat will still return a concatenated list when given two lists containing negative ints."""
    assert concat([1, -2, -3, 4], [0, -5, -7, 4]) == [1, -2, -3, 4, 0, -5, -7, 4]