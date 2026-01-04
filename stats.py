def get_num_words(content):
    "Counts the number of words in the given content string."
    words = content.split()
    return len(words)


def count_letters(content):
    """Counts each letter (case-insensitive) in the content and returns a dictionary."""
    letter_counts = {}
    for char in content.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts