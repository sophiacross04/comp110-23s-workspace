"""Quiz 2 practice question 2!"""

def value_exists(x: dict[str,int], y: int) -> bool:
    """Checks if value exists."""
    i: int = 0
    for elem in x:
        if y == x[elem]:
            return True
    return False