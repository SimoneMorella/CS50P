import sys

def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")

        else:
            l_count = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    if len(line.lstrip()) != 0 and not line.lstrip().startswith("#"):
                        l_count += 1
            print(l_count)

    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")


main()