import inflect

def main():
    p = inflect.engine()
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            print(f"Adieu, adieu, to {p.join(name_list)}")
            break


main()
