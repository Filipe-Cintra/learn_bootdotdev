def count_words(file):
    words = file.split()
    return len(words)

def count_chars(file):
    dict_chars = {}
    file = file.lower()

    for chars in file:
        dict_chars[chars] = dict_chars.get(chars, 0) + 1
    return dict_chars

def sort_on(char_tuple: tuple[str, int]) ->  int:
    return char_tuple[1]

def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    char_count = []
    for item in char_dict.items():
        char_count.append(item)
    sorted_char_count = sorted(char_count, reverse=True, key=sort_on)
    return sorted_char_count
        
