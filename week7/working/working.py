import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^(\d?\d):?(\d\d)? (AM|PM) to (\d?\d):?(\d\d)? (AM|PM)$", s
    ):
        start_h, start_m, start_t, end_h, end_m, end_t = matches.groups()
        start_h, end_h = int(start_h), int(end_h)
        if 1 <= start_h <= 12 and 1 <= end_h <= 12:
            if start_m and end_m:
                start_m, end_m = int(start_m), int(end_m)

                if start_m in range(60) and end_m in range(60):
                    if start_t == "PM" or end_t == "PM":
                        if start_t == "PM":
                            if start_h < 12:
                                start_h = start_h + 12

                        if end_t == "PM":
                            if end_h < 12:
                                end_h = end_h + 12

                    if start_t == "AM" or end_t == "AM":
                        if start_t == "AM" and start_h == 12:
                            start_h = 0

                        if end_t == "AM" and end_h == 12:
                            end_h = 0

                    return f"{start_h:02}:{start_m:02} to {end_h:02}:{end_m:02}"

                else:
                    raise ValueError
            else:
                if start_t == "PM" or end_t == "PM":
                    if start_t == "PM":
                        if start_h < 12:
                            start_h = start_h + 12

                    if end_t == "PM":
                        if end_h < 12:
                            end_h = end_h + 12

                if start_t == "AM" or end_t == "AM":
                    if start_t == "AM" and start_h == 12:
                        start_h = 0

                    if end_t == "AM" and end_h == 12:
                        end_h = 0

                return f"{start_h:02}:00 to {end_h:02}:00"

        else:
            raise ValueError

    else:
        raise ValueError


if __name__ == "__main__":
    main()
