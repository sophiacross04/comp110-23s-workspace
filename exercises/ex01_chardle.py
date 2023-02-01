"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730565129"

user_word: str = input("Enter a 5-character word: ")
count: int = 0

if (len(user_word) == 5): 
    user_letter: str = input("Enter a single character: ")

    if (len(user_letter) == 1): 
        print("Searching for " + user_letter + " in " + user_word)

        if (user_letter == user_word[0]): 
            print(user_letter + " found at index 0")
            count = count + 1
        if (user_letter == user_word[1]): 
            print(user_letter + " found at index 1")
            count = count + 1
        if (user_letter == user_word[2]): 
            print(user_letter + " found at index 2")
            count = count + 1
        if (user_letter == user_word[3]): 
            print(user_letter + " found at index 3")
            count = count + 1
        if (user_letter == user_word[4]): 
            print(user_letter + " found at index 4")
            count = count + 1

        if (count > 1): 
            print(str(int(count)) + " instances of " + user_letter + " found in " + user_word)
        else:
            if (count == 1): 
                print("1 instance of " + user_letter + " found in " + user_word)
            else:
                print("No instances of " + user_letter + " found in " + user_word)
    else:
        print("Error: Character must be a single character.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()