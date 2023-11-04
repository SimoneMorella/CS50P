def main():
    string = input("Input: ")
    new_string = ""
    for char in string:
        if char.islower():
            new_string += char.strip("aeiou")
        else:
            new_string += char.strip("AEIOU")
    print("Output:", new_string)


main()

