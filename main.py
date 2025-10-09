from stats import word_count
from stats import character_count
from stats import sort_count
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(word_count(get_book_text(path)))
    print("--------- Character Count -------")
    for i in sort_count(character_count(get_book_text(path))):
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()