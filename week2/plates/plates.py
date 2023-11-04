def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alpha = ''
    num = ''
    if s.isupper() and 2 <= len(s) <= 6 and s.isalnum() and s[0:2].isalpha():
        for char in s[2:]:
            if char.isalpha():
                alpha += char
            else:
                num += char
        if num != '':
            if not num[0] == "0" and s[s.index(num[0]):].isdecimal():
                return True
            else:
                return False
        else:
            return True
    else:
        return False

main()