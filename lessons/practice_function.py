"""Practice writing functions"""

def mimic (my_words: str, idx: int) -> str:
    """Given the string my_words, outputs the same string"""
    if idx >= len(my_words):
        return("Index too high")
    return my_words[idx]

print(mimic("Hello",8))