import random

# ── ASCII art for the hangman stages (0 = safe, 6 = dead) ──
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# ── Word bank with hints ──────────────────────────────────
WORD_BANK = [
    ("python",   "A popular programming language"),
    ("hangman",  "The name of this game"),
    ("laptop",   "A portable computer"),
    ("science",  "Study of the natural world"),
    ("guitar",   "A stringed musical instrument"),
    ("journey",  "A long trip or adventure"),
    ("oxygen",   "A gas we breathe"),
    ("blanket",  "Keeps you warm at night"),
    ("dolphin",  "An intelligent marine mammal"),
    ("eclipse",  "Sun blocked by the moon"),
]

MAX_WRONG = 6   # maximum incorrect guesses allowed


def display_banner():
    """Print a welcome banner for the game."""
    print("\n" + "=" * 50)
    print("        HANGMAN GAME  -- CodeAlpha")
    print("=" * 50)
    print("  Try to guess the hidden word letter by letter.")
    print(f"  You have {MAX_WRONG} incorrect guesses allowed.")
    print("=" * 50 + "\n")


def display_word(secret_word: str, guessed_letters: set) -> str:
    """Return the word with unguessed letters shown as underscores."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def display_status(secret_word: str, guessed_letters: set,
                   wrong_guesses: list, hint: str):
    """Print the current hangman figure, word progress, and game info."""
    print(HANGMAN_STAGES[len(wrong_guesses)])
    print(f"  Hint     : {hint}")
    print(f"  Word     : {display_word(secret_word, guessed_letters)}")
    print(f"  Letters  : {len(secret_word)} letters\n")

    if wrong_guesses:
        print(f"  Wrong    : {', '.join(sorted(wrong_guesses)).upper()}")
    else:
        print("  Wrong    : None yet")

    correct = [ch for ch in guessed_letters if ch in secret_word]
    if correct:
        print(f"  Correct  : {', '.join(sorted(correct)).upper()}")

    remaining = MAX_WRONG - len(wrong_guesses)
    print(f"  Chances  : {remaining} remaining\n")


def get_valid_guess(guessed_letters: set) -> str:
    """Prompt the player for a valid single alphabetic letter."""
    while True:
        guess = input("  Enter a letter: ").strip().lower()

        if len(guess) != 1:
            print("  Please enter exactly ONE letter.\n")
        elif not guess.isalpha():
            print("  Only alphabetic characters are allowed.\n")
        elif guess in guessed_letters:
            print(f"  You already guessed '{guess.upper()}'. Try another.\n")
        else:
            return guess


def play_game():
    """Run a single round of Hangman."""
    secret_word, hint = random.choice(WORD_BANK)
    guessed_letters: set = set()
    wrong_guesses: list = []

    print("\n  A new word has been chosen. Good luck!\n")

    while True:
        display_status(secret_word, guessed_letters, wrong_guesses, hint)

        # Check win condition
        if all(ch in guessed_letters for ch in secret_word):
            print("=" * 50)
            print("  CONGRATULATIONS! You guessed the word!")
            print(f"  The word was: {secret_word.upper()}")
            print("=" * 50 + "\n")
            return True

        # Check lose condition
        if len(wrong_guesses) >= MAX_WRONG:
            print(HANGMAN_STAGES[MAX_WRONG])
            print("=" * 50)
            print("  GAME OVER! You ran out of chances.")
            print(f"  The word was: {secret_word.upper()}")
            print("=" * 50 + "\n")
            return False

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"\n  Great! '{guess.upper()}' is in the word!\n")
        else:
            wrong_guesses.append(guess)
            print(f"\n  Oops! '{guess.upper()}' is NOT in the word.\n")


def main():
    """Entry point — handles multiple rounds and scorekeeping."""
    display_banner()
    wins = 0
    losses = 0

    while True:
        result = play_game()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"  Score  -->  Wins: {wins}  |  Losses: {losses}\n")
        again = input("  Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thanks for playing Hangman! -- CodeAlpha\n")
            break


if __name__ == "__main__":
    main()
