"""Challenge question 04 - Dict function writing."""

def zip(strs: list[str], ints: list[int]) -> dict[str, int]:
    """Creates a dictionary"""
    d: dict[str, int] = dict()
    i: int = 0
    if (len(strs) != len(ints)) or (len(strs) == 0) or (len(ints) == 0):
        return d
    while i < len(strs):
        d[strs[i]] = ints[i]
        i += 1
    return d