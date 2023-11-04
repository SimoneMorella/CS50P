def main():
    h_m = input("What time is it? ")
    if not convert(h_m):
        print("Insert a valid time")

    elif 7 <= convert(h_m) <= 8:
        print("breakfast time")

    elif 12 <= convert(h_m) <= 13:
        print("lunch time")

    elif 18 <= convert(h_m) <= 19:
        print("dinner time")



def convert(time):
    hour, minute = time.split(":")
    if 00 <= int(hour) <= 23 and 00 <= int(minute) <= 59:
        minute = float(int(minute) / 60)
        time = float(int(hour) + minute)
        return time
    else:
        return False

if __name__ == "__main__":
    main()