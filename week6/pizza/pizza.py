import sys
from csv import DictReader
from tabulate import tabulate

def main():
    menu = []
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")

        else:

            with open(sys.argv[1]) as file:
                reader = DictReader(file)
                for row in reader:
                    menu.append(row)
            print(tabulate(menu,headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
    except IndexError:
        sys.exit("Too few command-line arguments")


main()