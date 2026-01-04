from stats import get_num_words, count_letters
from sys import argv

def get_book_text(file_path):
    "Reads the contents of the file at file_path and returns it as a string."
    with open(file_path) as f:
        content = f.read()
    return content

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        raise SystemExit (1)
    else:
        file_path = argv[1]

    content = get_book_text(file_path)
    num_words = get_num_words(content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Count and print letter frequencies
    letter_counts = count_letters(content)
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    print("--------- Character Count -------")
    for char, count in sorted_counts:
        print(f"{char}: {count}")
    print("============= END ===============")

main()