from stats import word_count, char_count

def get_book_text(path_to_book):
    with open(path_to_book) as b:
        book_contents = b.read()
    
    return book_contents    
        

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    #print(text)
    print(f"{num_words} words found in the document")
    print(char_count(text))
    
    
main()