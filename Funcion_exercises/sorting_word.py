"""Sort hyphen-separated word alphabetically."""


def sort_words(text):
    """Return the word sorted and joined with hyphens."""
    words = text.split("-")
    words.sort()
    return "-".join(words)

result = sort_words("python-variable-function-computer-monitor")
print(result)
