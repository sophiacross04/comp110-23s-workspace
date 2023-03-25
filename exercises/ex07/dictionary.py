"""Dictionary!"""

__author__: str = "730565129"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    output: dict[str, str] = dict()
    for key in input:
        if input[key] in output:
            raise KeyError("Oh no, you have more than one of the same key!")
        output[input[key]] = key
    return output


def favorite_color(colors: dict[str, str]) -> str:
    """Returns color that appears most frequently."""
    counts: dict[str, int] = dict()
    favorite: str = ""
    i: int = 0
    for name in colors:
        if colors[name] in counts:
            counts[colors[name]] += 1
        else:
            counts[colors[name]] = 1
    for color in counts:
        if counts[color] > i:
            i = counts[color]
            favorite = color
    return favorite


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of times a value is in the input list."""
    output: dict[str, int] = dict()
    for item in input:
        if item in output:
            output[item] += 1
        else: 
            output[item] = 1
    return output