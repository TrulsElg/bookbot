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

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = count_words(content=file_contents)
    print(f"{word_count} words found in the document")
    print()
    
    letter_count = sorted(count_letters(file_contents).items(), key=lambda d: d[1], reverse=True)
    for l in letter_count:
        print(f"The '{l[0]}' character was found {l[1]} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()