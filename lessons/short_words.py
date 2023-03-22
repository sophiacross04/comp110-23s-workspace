"""Quiz 2 practice."""
__author__: str = "730565129"


def short_words(x: list[str]) -> list[str]:
    """Will return a list of words that are shorter than 5 characters."""
    new: list[str] = []
    for elem in x:
        if len(elem) < 5:
            new.append(elem)
        else:
            print(f"{elem} is too long!")
    return new