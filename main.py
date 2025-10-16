from stats import get_word_count, get_character_count, sort
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_contents = get_book_text(sys.argv[1])
    word_count = get_word_count(book_contents)
    character_dict = get_character_count(book_contents)
    sorted_character_list = sort(character_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_character_list:
        print(f"{character['name']}: {character['num']}")
    print("============= END ===============")

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

main()