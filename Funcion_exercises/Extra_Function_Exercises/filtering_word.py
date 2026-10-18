"""Filter word by their length"""

def filter_word(words, n):
    """Return a new list of word with more than n letters."""
    filtered_words = []

    for word in words:
        if len(word) > n:
            filtered_words.append(word)

    return filtered_words

word_list = ["cloud", "sun", "wonderful", "day"]
letters_limit = int(input("Enter the number of letters to exceed: "))

result = filter_word(word_list, letters_limit)
print(result)
