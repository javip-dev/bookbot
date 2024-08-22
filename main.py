def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    n_words = count_words(text)
    print(n_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text : str):
    words = text.split()
    return len(words)

main()