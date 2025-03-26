"""Writing a program to create a game like Wordle! I love NYT Games"""

__author__: str = "730678501"


def contains_char(word: str, character: str) -> bool:
    """Check if a given character is present in the provided word"""
    assert len(character) == 1, f"len('{character}') is not 1"

    index = 0
    while index < len(word):
        if word[index] == character:
            return True
        index += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of colored blocks to indicate correctness of guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result = ""
    index = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1

    return result


def input_guess(length: int) -> str:
    """Prompts the user for a guess of an expected length"""
    guess = input(f"Enter a {length} character word:")

    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop!"""
    turns = 1
    max_turns = 6
    won = False

    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            won = True
        else:
            turns += 1
    if won:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
