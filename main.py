def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    dict_list = convert_to_dict_list(chars_dict) 
    dict_list.sort(reverse=True, key=sort_on)
    sorted_dict_list = sorted(dict_list, reverse=True, key=sort_on)
    dict_report = report(book_path, num_words, sorted_dict_list)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def convert_to_dict_list(dict): 
    dict_list = []
    for key, value in dict.items(): 
        if key.isalpha() == True: 
            dict_list.append({"char": key, "num": value})
    return dict_list

def sort_on(dict): 
    return dict["num"]


def report(book_path, num_words,text_dict):
    print(f"--- Begin report of {book_path} ---") 
    print(f"{num_words} words found in the document") 
    for c in text_dict: 
        print(f"The '{c["char"]}' character was found {c["num"]} times")
    print(f"--- End report ---")

main()