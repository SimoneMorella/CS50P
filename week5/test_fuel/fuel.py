def main():
    fraction = input("Fraction: ")
    tank_v = convert(fraction)
    print(f"{gauge(tank_v)}")


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return int(round(x / y, 2) * 100)

def gauge(tank_value):
    if tank_value <= 1:
        return "E"
    elif tank_value >= 99:
        return "F"
    else:
        return f"{tank_value}%"


if __name__ == "__main__":
    main()