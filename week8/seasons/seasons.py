from datetime import date
import sys, re, inflect


def main():
    p = inflect.engine()
    year, month, day = [int(i) for i in get_n_check()]
    minutes = subtraction(year, month, day)
    number_word = p.number_to_words(minutes, andword="").capitalize()
    print(f"{number_word} minutes")


def get_n_check():
    input_date = input("Date of birth: ")
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", input_date):
        return matches.groups()
    else:
        sys.exit("Invalid date")


def subtraction(year, month, day):
    today = date.today()
    birthday = date(year, month, day)
    time_diff = today - birthday
    return time_diff.days * 24 * 60


if __name__ == "__main__":
    main()
