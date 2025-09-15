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