"""Introducing user input and named constants"""

SECRET: str = "punk"


def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    # TODO 1: If different lengths, not same word
    if len(word) != len(secret):
        print("Words are different lengths.")
        return False
    # (If we reach this point, we know the words are the same length)
    # TODO 2: if we have more letters to check...
    if idx < len(word):
        # Check to see if the next pair of letters are the same!
        if word[idx] != secret[idx]:
            print(f"{word[idx]} isn't the secret word's next letter.")
            return False
        else:
            print(f"{word[idx]} is at index {idx} for both! Checking next letters...")
            return guess_secret(word=word, secret=secret, idx=idx + 1)
        # TODO 3: every letter matches and none left
    print("They are the same word!")
    return True


print(guess_secret(word=input("What if your word "), secret=SECRET))
