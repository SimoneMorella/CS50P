import sys
from csv import DictReader, DictWriter

def main():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    else:
        clean(sys.argv[1], sys.argv[2])


def clean(input, output):
    students = []
    n_students = []
    try:
        with open(input, "r") as file:
            reader = DictReader(file)
            for row in reader:
                students.append(row)

            for student in students:
                last, first = student["name"].split(", ")
                n_students.append({"first": first, "last": last, "house": student["house"]})

            with open(output, "w") as wfile:
                writer = DictWriter(wfile, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in n_students:
                    writer.writerow(row)

    except  FileNotFoundError:
        sys.exit(f"Could not read {input}")

if __name__ == "__main__":
    main()
