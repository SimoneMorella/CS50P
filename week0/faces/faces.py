def main():
    sentence = input("Say something and add an emoji: ")
    converted_sentence = convert(sentence)
    print(converted_sentence)

def convert(string):
    new_string = string.replace(":)", "🙂").replace(":(", "🙁")
    return new_string

main()
