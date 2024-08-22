def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dic = get_chars_dic(text)
    print(chars_dic)
   # print(num_words)


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


def get_num_words(text : str):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()