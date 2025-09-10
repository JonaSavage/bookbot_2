def word_count(book_text):
    count = len(book_text.split())
    return count


def char_count(book_text):
    to_lower = book_text.lower()
    char_dict = {}
    for c in to_lower:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    
    return char_dict