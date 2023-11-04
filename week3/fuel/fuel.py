def main():
    tank_fuel = tank()
    if tank_fuel <= 1:
        print("E")
    elif tank_fuel >= 99:
        print("F")
    else:
        print(f"{tank_fuel}%")


def tank():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)
            if x > y:
                pass
            else:
                value = round(x / y, 2) * 100
                return int(value)
        except (ValueError):
            pass
        except ZeroDivisionError:
            pass

main()