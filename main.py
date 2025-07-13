import sys

if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main ():
    from stats import word_count
    words = word_count(sys.argv[1])


    from stats import sort
    letters = sort(sys.argv[1])

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for letter in letters:
        print(f"{letter[0]}: {letter[1]}")
    print("============= END ===============")

main()
