import sys
from stats import get_num_words, sort_list
from stats import count_letters


def get_book_text(filepath: str):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

print("============ BOOKBOT ============")
content = get_book_text(path)
print("----------- Word Count ----------")
num_words = get_num_words(content)
print(f"Found {num_words} total words")
print("--------- Character Count -------")
stats = count_letters(content)
sorted = sort_list(stats)
for pair in sorted:
    if pair["char"].isalpha():
        print(f"{pair['char']}: {pair['num']}")

print("============= END ===============")
