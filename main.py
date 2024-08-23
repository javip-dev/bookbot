def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dic = get_chars_dic(text)
    print_report(book_path,num_words,chars_dic)


def get_chars_dic(text: str):
    chars = {}
    for char in text:
        if char.isalpha():
            lowered = char.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
               chars[lowered] = 1 
    return chars


def print_report(path , num_words, chars_dic: dict):
    print(f"-- Begin report of {path}")
    print(f"{num_words} found in the document")
    print("\n")
    list_from_dict = list(chars_dic.items())
    list_chars_dic = []
    for tuple in list_from_dict:
        dic_temp = {}
        dic_temp["letter"] = tuple[0]
        dic_temp["num"] = tuple[1]
        list_chars_dic.append(dic_temp)
    list_chars_dic.sort(reverse=True, key=sort_on)
    for l in list_chars_dic:
        print(f"The '{l['letter']}' character was found {l['num']} times")
    print("--- End report ---")
    

def sort_on(dict):
    return dict["num"]


def get_num_words(text : str):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()