"""Question 1: Odd and Even!"""

def odd_and_even(nums: list[int]) -> list[int]:
    """Returns new list containing elements that are odd at an even index."""
    i: int = 0
    new: list[int] = []
    while i < len(nums):
        if i % 2 == 0:
            if nums[i] % 2 != 0:
                new.append(nums[i])
        i += 1
    return new
