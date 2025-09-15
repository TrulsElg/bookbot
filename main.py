from stats import count_words, count_letters, sort_dictionary

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print("----------- Word Count ----------")
    word_count = count_words(content=file_contents)
    print(f"{word_count} words found in the document")

    print("--------- Character Count -------")
    sorted_letters = sort_dictionary(count_letters(file_contents))
    for l in sorted_letters:
        print(f"The '{l[0]}' character was found {l[1]} times")

    print("============= END ===============")

if __name__ == "__main__":
    main()