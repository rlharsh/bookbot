def main():
    book_path = "books/frankenstein.txt"
    # text = get_book_text(book_path)
    #print(text)
    #word_count = count_words(text)
    #print(word_count)
    #letter_count = get_letter_count(text)
    #print(letter_count)
    print_report(book_path)


def print_report(book_path):
    text_contents = get_book_text(book_path)
    word_count = count_words(text_contents)
    chars = get_letter_count(text_contents)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char in chars:
        print(f"The '{char['char']}' character was found {char['num']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(item):
    return item["num"]


def get_letter_count(text):
    charmap = {}
    text = text.lower()  # Normalize to lowercase

    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in charmap:
                charmap[char] += 1
            else:
                charmap[char] = 1

    # Convert the dictionary to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in charmap.items()]

    # Sort the list of dictionaries by the "num" key in descending order
    char_list.sort(reverse=True, key=sort_on)

    return char_list



def count_words(text):
    word_count = len(text.split())
    return word_count


main()
