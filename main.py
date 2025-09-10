from stats import *

def get_book_text(path_to_book):
    with open(path_to_book) as b:
        book_contents = b.read()
    
    return book_contents    
        

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    sorted_dictionary = sort_dics(char_count(text))
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted_dictionary)):
        if sorted_dictionary[i]["char"].isalpha():
            print(f"{sorted_dictionary[i]["char"]}: {sorted_dictionary[i]["num"]}")
    print("============= END ===============")
    
    
main()