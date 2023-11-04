def main():
    camelcase = input("CamelCase: ")
    snake_case = convert(camelcase)
    print("snake_case:", snake_case)

def convert(input):
    converted = ""
    for char in input:
        if char.isupper():
            char = "_" + char.lower()
        converted += char
    return converted

main()