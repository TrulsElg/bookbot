import json


def count_words(content):
    return len(content.split())

def count_letters(content):
    letter_dict = dict()

    for char in content:
        if char.isalpha():
            c = char.lower()
            if c in letter_dict:
                letter_dict[c] += 1
            else:
                letter_dict[c] = 1

    return letter_dict

def sort_dictionary(dictionary):
    return sorted(dictionary.items(), key=lambda d: d[1], reverse=True)

def analyze_book(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    with open(book_path) as f:
        file_contents = f.read()

    print("----------- Word Count ----------")
    word_count = count_words(content=file_contents)
    print(f"Found {word_count} total words found in the document")

    print("--------- Character Count -------")
    sorted_letters = sort_dictionary(count_letters(file_contents))
    for l in sorted_letters:
        if not l[0].isalpha():
            continue
        print(f"{l[0]}: {l[1]}")

    print("============= END ===============")