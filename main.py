def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

        print(len(words))
        print(letter_count(words))

def letter_count(words):
    letter_count = {}

    for word in words:
        lowered_word = word.lower()
        for character in lowered_word:
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1
    
    return letter_count

main()