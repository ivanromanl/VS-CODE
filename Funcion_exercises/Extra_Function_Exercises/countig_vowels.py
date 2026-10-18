"""Counting vowels in a string"""


def count_vowels(text):
    """Return the number of vowels in a text."""
    vowels = "aeiouáéíóúü"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    return count

user_text = input("Enter a text: ")
result =count_vowels(user_text)
print(result)
