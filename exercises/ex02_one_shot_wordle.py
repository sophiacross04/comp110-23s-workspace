"""One shot Wordle!"""

__author__ : 730565129

#naming variables
secret_word: str = "python"
user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
index_guess: int = 0
index_secret: int = 1
emoji: str = ""
count: int = 0

#naming emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#checking if input is the same length as secret word
while(len(user_guess) != len(secret_word)):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

#checking if input is the same word as the secret word
while(index_guess < len(secret_word)):
    if(user_guess[index_guess] == secret_word[index_guess]):
        emoji = emoji + GREEN_BOX
    else:
        while(index_secret < len(secret_word)):
            if(user_guess[index_guess] == secret_word[index_secret]):
                count = count + 1
            index_secret = index_secret + 1
        if(count > 0):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index_guess = index_guess + 1
    count = 0
    index_secret = 0

#show if letters are the same
print(emoji)

if(user_guess == secret_word):
    print(f"Woo! You got it!")
else:
    print(f"Not quite. Play again soon!")
