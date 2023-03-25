"""Dictionary test!"""

__author__: str = "730565129"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_empty() -> None:
    """Invert edge case: tests if inverting an empty dict will return an empty dict."""
    assert invert({}) == {}


def test_invert_one() -> None:
    """Invert use case 1: tests if inverting a dict with one key/value pair will return the inverted pair."""
    test: dict[str, str] = {'a': '1'}
    assert invert(test) == {'1': 'a'}


def test_invert_multi() -> None:
    """Invert use case 2: tests if inverting a dict with multiple key/value pairs will return an inverted dict."""
    test: dict[str, str] = {'a': '1', 'b': '2', 'c': '3'}
    assert invert(test) == {'1': 'a', '2': 'b', '3': 'c'}


def test_color_empty() -> None:
    """Favorite_color edge case: tests if inputting an empty dict will return an empty string."""
    assert favorite_color({}) == ""


def test_color_multi() -> None:
    """Favorite_color use case 1: tests if inputting a dict with multiple key/value pairs will return a string with the color that appears most frequently."""
    test: dict[str, str] = {'a': 'blue', 'b': 'blue', 'c': 'red'}
    assert favorite_color(test) == "blue"


def test_color_same() -> None:
    """Favorite_color use case 2: tests if there is a tie for the favorite color then the color that appears first is returned."""
    test: dict[str, str] = {'a': 'blue', 'b': 'red', 'c': 'blue', 'd': 'red'}
    assert favorite_color(test) == "blue"


def test_count_empty() -> None:
    """Count edge case: tests if an empty list will return an empty dict."""
    assert count([]) == {}


def test_count_one() -> None:
    """Count use case 1: tests if a list with one value will return a dict with one key/value pair."""
    test: list[str] = ["one"]
    assert count(test) == {'one': 1}


def test_count_multi() -> None:
    """Count use case 2: tests if a list with multiple values will return the correct number of counts for each value."""
    test: list[str] = ["one", "two", "two", "three", "three", "three"]
    assert count(test) == {'one': 1, 'two': 2, 'three': 3}