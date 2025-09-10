def word_count(book_text):
    count = len(book_text.split())
    return count

def sort_on(items):
    return items["num"]


def char_count(book_text):
    to_lower = book_text.lower()
    char_dict = {}
    for c in to_lower:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    
    return char_dict


def sort_dics(book_dic):
    stats_list = []
    temp_dic = {}
    
    for c in book_dic:
        temp_dic = {"char": c, "num": book_dic[c]}
        stats_list.append(temp_dic)
        
    stats_list.sort(reverse=True, key=sort_on)
    return stats_list      