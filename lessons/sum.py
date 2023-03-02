"""Example function for unit tests."""

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    for item in range(0,len(xs)):
        sum_total += xs[item]
    return sum_total
