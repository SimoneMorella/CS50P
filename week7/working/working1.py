import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search("^(\d?\d):?(\d\d)? (AM|PM) to (\d?\d):?(\d\d)? (AM|PM)$", s):
        if len(matches.groups()) == 6:
            start_h, start_m, start_t, end_h, end_m, end_t = matches.groups()
            print(start_t)
            start_h, start_m, end_h, end_m = int(start_h), int(start_m), int(end_h), int(end_m)
            if 1 <= int(start_h) <= 12 and 1 <= int(end_h) <= 12:
                if int(start_m) in range(60) and int(end_m) in range(60):
                    start_h = 12
                    return start_h
                else:
                    raise ValueError
            else:
                raise ValueError
    else:
        raise ValueError

if __name__ == "__main__":
    main()