def word_count(file_path):    
    """
    Main function to read and count the words in the content of a book file.
    """
    try:
        with open(f"{file_path}", 'r') as file:
            split_content = []
            content = file.read()
            split_content = content.split(sep=None)
            word_count = len(split_content)
            return word_count
            

    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")


def letter_count(file_path):
    """
    Function to count the number of each letter in the book file.
    """
    alphaphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 
                  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
                  'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                  'x', 'y', 'z')
    alphaphabet_count = {letter: 0 for letter in alphaphabet}
    # This function counts the number of letters in the book file.

    try:
        with open(f"{file_path}", 'r') as file:
            content = file.read()
            for letter in content.lower():
                if letter in alphaphabet_count:
                    alphaphabet_count[letter] += 1
        return alphaphabet_count
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
    
def sort(file_path):
    """
    Function to sort the letter counts in descending order.
    """
    letter_counts = letter_count(file_path)
    sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts