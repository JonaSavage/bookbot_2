from stats import *
import sys

def get_book_text(path_to_book):
    with open(path_to_book) as b:
        book_contents = b.read()
    
    return book_contents    
        

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text = get_book_text(sys.argv[1])
    num_words = word_count(text)
    sorted_dictionary = sort_dics(char_count(text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted_dictionary)):
        if sorted_dictionary[i]["char"].isalpha():
            print(f"{sorted_dictionary[i]["char"]}: {sorted_dictionary[i]["num"]}")
    print("============= END ===============")
    
    
main()