"""EX06 - Choose your own adventure!"""

__author__: str = "730565129"

from random import randint

# establishing global variables
points: int = 0
player: str = ""
choice: int = 0
doom: int = 1
monster: int = 0

# named constants (emojis)
EMOJI_QUEST: str = "\U0001F914"
EMOJI_SWORD: str = "\U0001F44A"
EMOJI_EXIT: str = "\U0000274E"
EMOJI_WIN: str = "\U0001F973"
EMOJI_LOSE: str = "\U0001F480"
EMOJI_QMARK: str = "\U00002753"
EMOJI_CHECK: str = "\U00002705"
EMOJI_X: str = "\U0000274C"
EMOJI_MENU: str = "\U0001F3AE"
EMOJI_LIGHT: str = "\U0001F6A8"
EMOJI_MONSTER: str = "\U0001F47E"


# main code
def main() -> None:
    """Main code of program."""
    global points
    global doom
    greet()
    while True is True:
        print(f"{3 * EMOJI_MONSTER} MONSTER BATTLE {3 * EMOJI_MONSTER}")
        print(f"{player}, you currently have a {points} point bonus!")
        options()
        if choice == 1:
            questions() 
        if choice == 2:
            points = battle(points)
            if points > monster:
                print(f"{3 * EMOJI_WIN} VICTORY! {3 * EMOJI_WIN}\nGood work {player}, you slayed the monster!\nAs a reward, you have recieved 5 points!")
                points += 5
                doom *= 2
            else:
                print(f"{3 * EMOJI_LOSE} You lost! {3 * EMOJI_LOSE}\nThe monster is still on the loose, make sure you're ready before you battle again!\nBecause you lost, you lost all your points!")
                points = 0
                doom = 1
        if choice == 3:
            bye()


# greet function
def greet() -> None:
    """Greets player and asks for name."""
    global player
    print("Welcome to my choose your adventure game! In this game, you will battle a monster with the power of math!")
    print("How it works:\n- Battle the monster by playing a guessing game\n- Earn bonus points to prepare for battle with challenge questions\n- Beware: the more times you win, the harder it is to beat the monster!\n- Have fun!")
    player = input("What is your name? ")
    print(f"Hello, {player}! I hope you enjoy my game!")


# presents three options
def options() -> None:
    """User gets to choose which option they want."""
    global choice
    print(f"{EMOJI_MENU} Game menu: {EMOJI_MENU}\n1. {EMOJI_QUEST}: Earn some points with challenge questions!\n2. {EMOJI_SWORD}: Battle the monster!\n3. {EMOJI_EXIT}: Exit the game!")
    choice = int(input("Which option would you like? "))
    print(f"You chose Option {choice}! Great choice!")


# one custom procedure
def questions() -> None:
    """Answer math questions to earn point bonuses!"""
    global points
    num1: int = 0
    num2: int = 0
    answer: int = 0
    type: int = 0
    i: int = 0
    print(f"{3 * EMOJI_QUEST} CHALLENGE QUESTIONS {3 * EMOJI_QUEST}")
    while i < 5:
        print(f"{3 * EMOJI_QMARK} Question {i + 1} {3 * EMOJI_QMARK}")
        type = randint(1, 50)
        if type % 2 == 0:
            num1 = randint(1, 10)
            answer = int(input(f"What is the square root of {num1 ** 2}? "))
            if answer == num1:
                print(f"{EMOJI_CHECK} Correct! You earned a bonus point!")
                points += 1
            else:
                print(f"{EMOJI_X} Wrong! Better luck next time!")
        elif type % 3 == 0:
            num1 = randint(1, 5)
            num2 = randint(1, 5)
            answer = int(input(f"What is {num1} ** {num2}? "))
            if answer == (num1 ** num2):
                print(f"{EMOJI_CHECK} Correct! You earned a bonus point!")
                points += 1
            else:
                print(f"{EMOJI_X} Wrong! Better luck next time!")
        else:
            num1 = randint(1, 5)
            num2 = randint(1, 3)
            answer = int(input(f"Given the equation {num1}x = {num2 * num1}, what is x? "))
            if answer == num2:
                print(f"{EMOJI_CHECK} Correct! You earned a bonus point!")
                points += 1
            else:
                print(f"{EMOJI_X} Wrong! Better luck next time!")
        i += 1
    print(f"Good job {player}, you made it through all the challenge questions!")


# one custom function
def battle(num: int) -> int:
    """Battle!"""
    global monster
    print(f"{3*EMOJI_SWORD} BATTLE {3*EMOJI_SWORD}")
    i: int = 0
    p_health: int = 100
    m_health: int = 100
    secret: int = 0
    user: int = 0
    while i < 3:
        print(f"{3*EMOJI_LIGHT} ROUND {i + 1} {3*EMOJI_LIGHT}")
        if m_health < 0:
            m_health == 0
        if p_health < 0:
            p_health == 0
        print(f"Points: {num}")
        print(f"Health points:\n- {player}: {p_health}\n- Monster: {m_health}")
        secret = randint(1, 3)
        user = int(input("Pick a number 1 - 3! "))
        if user == secret:
            print(f"Good job {player}, you picked the magic number!\nYou did {num * secret} damage to the monster!\nYou earned another point!")
            m_health -= (num * user)
            num += 1
        else:
            print(f"Oh no, the monster won this round!\nThe monster did {secret * doom} damage to you!\nYou lost 2 points!")
            p_health -= (secret * doom)
            num -= 2
        i += 1
    return num


# another custom procedure
def bye() -> None:
    """Exits the game!"""
    print(f"{3*EMOJI_EXIT} EXIT {3*EMOJI_EXIT}")
    print(f"Bye {player}, I'm so sad to see you go!\nYou ended with {points} points.\nHope you play again soon!")
    quit()


# initial call to main
if __name__ == "__main__":
    main()