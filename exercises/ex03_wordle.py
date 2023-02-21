"""Ex03 - Structured Wordle!"""

__author__: str = "730565129"


def contains_char(secret: str, letter: str) -> bool:
    """Checks if the letter is in the secret word!"""
    assert len(letter) == 1
    # makes sure letter is only 1 char

    i: int = 0

    while i < len(secret):
        # checks each idx of secret for the letter
        if letter == secret[i]:
            return True
        i = i + 1
    return False


def mult_s(secret: str, letter: str) -> int:
    """Checks how many of each letter is in the secret word!"""
    assert len(letter) == 1
    # makes sure letter is only 1 char

    i: int = 0
    c: int = 0

    while i < len(secret):
        # checks each idx of secret for the letter
        if letter == secret[i]:
            c = c + 1
        i = i + 1
    return c


def mult_g(guess: str, letter: str) -> int:
    """Checks how many of each letter is in the guess!"""
    assert len(letter) == 1
    # makes sure letter is only 1 char

    i: int = 0
    c: int = 0

    while i < len(guess):
        # checks each idx of secret for the letter
        if letter == guess[i]:
            c = c + 1
        i = i + 1
    return c


def emojified(guess: str, secret: str) -> str:
    """Produces an emoji Wordle!"""
    assert len(secret) == len(guess)

    # emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i: int = 0
    emojis: str = ""
    
    
    while i < len(secret):
        c: int = mult_s(secret,guess[i])
        g: int = mult_g(guess,guess[i])
        
        if secret[i] == guess[i]:
            emojis = emojis + GREEN_BOX
        elif (not contains_char(secret, guess[i])) or (g > c):
            emojis = emojis + WHITE_BOX
        elif (contains_char(secret, guess[i])):
            emojis = emojis + YELLOW_BOX
        
        i = i + 1
    
    return emojis


def input_guess(expected_len: int) -> str:
    """Makes sure guess is same length as expected!"""
    word: str = input(f"Enter a {expected_len} character word: ")

    while len(word) != expected_len:
        word = input(f"That wasn't {expected_len} chars! Try again: ")
    
    return word


def main() -> None:
    """The entrypoint of the program and the main game code!"""
    # establishing variables
    secret: str = "codes"
    turns: int = 1
    win: bool = False

    while (turns <= 6) and (win is False):
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            win = True
        else:
            turns = turns + 1
    
    if win:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


# runs main program
if __name__ == "__main__":
    main()