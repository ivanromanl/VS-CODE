# Find Words Longer Than Four Letters
words = []
for i in range(5):
    word = input(f"Enter word {i + 1}: ")
    words.append(word)

long_words = []

for word in words:
    if len(words) > 4:
        long_words.append(word)

print(f"New list: {long_words}")