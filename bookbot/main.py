import sys
from stats import count_words, count_chars, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path, 'r') as f:
        file_contents = f.read()
        return file_contents

def print_report(path, word_count, sorted_list):
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""",)
    for word, num in sorted_list:
        if word.isalpha():
            print(f"{word}: {num}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    chars_dict = count_chars(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(path, num_words, sorted_list)

    
   

if __name__ == "__main__":
    main()