def main():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)
                month = f"{month:02}"
                day = '{:02}'.format(day)
                year = '{:04}'.format(year)
                convert(month, day, year)
                break

            else:
                month, day, year = date.split()
                if "," in day:
                    day, year = int(day.removesuffix(",")), int(year)
                    month = month.capitalize()
                    day = '{:02}'.format(day)
                    year = '{:04}'.format(year)
                    convert(month, day, year)
                    break
                else:
                    raise ValueError

        except ValueError:
            pass


def convert(month, day, year):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    if month.isalpha() and month in months and 1 <= int(day) <= 31:
        print(f"{year}-{months.index(month) + 1:02}-{day}")

    elif month.isdecimal() and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
        print(f" {year}-{month}-{day}")

    else:
        raise ValueError

main()





