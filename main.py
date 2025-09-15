import sys
from stats import analyze_book

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    analyze_book(sys.argv[1])

if __name__ == "__main__":
    main()