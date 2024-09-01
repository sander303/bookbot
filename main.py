def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    wordcount = get_book_wordcount(text)

    characters_dict = get_character_count(text)

    character_report = get_character_report(characters_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordcount} words found in the document")
    print()
    for character in character_report:
        print(f"The '{character['letter']}' character was found {character['count']} times")
    print("--- End of report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_wordcount(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_counts = {}
    lowercase_text = text.lower()
    for character in lowercase_text:
        if character not in character_counts:
            character_counts[character] = 1
        else:  
            character_counts[character] += 1
    return character_counts

def sort_on(dict):
    return dict["count"]

def get_character_report(dict):
    sorted_characters = []
    for character in dict:
        if character.isalpha():
            list_entry = {"letter": character, "count": dict[character]}
            sorted_characters.append(list_entry)
    
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters


main()
