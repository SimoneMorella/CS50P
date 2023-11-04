import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    check = 0
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for num in matches.groups():
            if int(num) in range(256):
                check += 1
        if check == 4:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()