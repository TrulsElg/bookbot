def count_words(content):
    return len(content.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    print(count_words(file_contents))

if __name__ == "__main__":
    main()