from stats import count_words, count_letters, sort_dictionary

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    with open("books/frankenstein.txt") as f:
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

if __name__ == "__main__":
    main()