def count_words(content):
    return len(content.split())

def count_letters(content):
    letter_dict = dict()

    lines = "".join(content.split("\n"))
    for char in lines:
        if char.isalpha():
            c = char.lower()
            if c in letter_dict.keys():
                letter_dict[c] += 1
            else:
                letter_dict[c] = 1

    return letter_dict

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    print(count_letters(file_contents))

if __name__ == "__main__":
    main()