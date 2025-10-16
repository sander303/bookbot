def get_word_count(text):
    array_of_words = text.split()
    word_count = len(array_of_words)
    return word_count

def get_character_count(text):
    character_dict = {}
    lowercase_text = text.lower()
    for character in lowercase_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(items):
    return items["num"]

def sort(character_dict):
    dict_list = []
    new_dict = {}
    for entry in character_dict:
        if entry.isalpha():
            new_dict["name"] = entry
            new_dict["num"] = character_dict[entry]
            dict_list.append(new_dict)
            new_dict = {}
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

