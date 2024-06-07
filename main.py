def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

        print("--- Begin report of books/frankenstein.txt ---")

        print(f"{len(words)} words found in the document\n")
        letter_count(words)

        print("--- End report ---")

def letter_count(words):

    letter_count = {}

    for word in words:
        lowered_word = word.lower()
        for character in lowered_word:
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1
    
    sorted_letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))

    for key, value in sorted_letter_count.items():
        print(f"The '{key}' character was found {value} times ")

main()