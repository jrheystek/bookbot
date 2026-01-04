from stats import get_num_words, count_letters

def get_book_text(file_path):
    "Reads the contents of the file at file_path and returns it as a string."
    with open(file_path) as f:
        content = f.read()
    return content

def main():
    file_path = "books/frankenstein.txt"
    content = get_book_text(file_path)
    num_words = get_num_words(content)
    print(f"Found {num_words} total words.")

    # Count and print letter frequencies
    letter_counts = count_letters(content)
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    print("\nLetter frequencies (sorted):")
    for char, count in sorted_counts:
        print(f"'{char}': {count}")

main()