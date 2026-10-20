def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    words = content.split()
    word_count = len(words)
    print(f"The file '{filename}' contains {word_count} words.")

def main():
    filename = input("Enter the filename (including extension): ")
    count_words(filename)

if __name__ == "__main__":
    main()