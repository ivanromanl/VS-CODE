"""Count how many times a character appears in a text."""


def count_character(text, character):
    """Return the number of occurrences of the character."""
    count = 0

    for letter in text:
        if letter == character:
            count += 1

    return count


user_text = input("Enter a text: ")
user_character = input("Enter the character to search for: ")

result = count_character(user_text, user_character)
print(f"The character was found {result} times.")
