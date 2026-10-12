"""Count uppercase and lowercase letters in a string."""


def count_letters(text):
    """Print the number of uppercase and lowercase letters."""
    uppercase_count = 0
    lowercase_count = 0

    for character in text:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1

    print(
        f"There are {uppercase_count} uppercase letters "
        f"and {lowercase_count} lowercase letters."
    )


count_letters("I love python code")
