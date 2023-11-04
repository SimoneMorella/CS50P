def main():
    string = input("Input: ")
    new_string = shorten(string)
    print("Output:", new_string)

def shorten(word):
    short_word = ""
    for char in word:
        if char.islower():
            short_word += char.strip("aeiou")
        else:
            short_word += char.strip("AEIOU")
    return short_word

if __name__ == "__main__":
    main()

