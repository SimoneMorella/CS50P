import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x, y = generate_integer(level), generate_integer(level)
        errors = 0
        while True:
            try:
                answer = input(f"{x} + {y} = ")
                if int(answer) != (x + y):
                    print("EEE")
                    errors += 1
                    if errors == 3:
                        print(f"{x} + {y} = {x + y}")
                        i += 1
                        break
                else:
                    score += 1
                    i += 1
                    break
            except ValueError:
                print("EEE")
                errors += 1
                if errors == 3:
                    print(f"{x} + {y} = {x + y}")
                    i += 1
                    break
                pass
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        range_start = 0
        range_end = 10**(level) - 1
        return random.randint(range_start, range_end)
    else:
        range_start = 10**(level -1)
        range_end = 10**(level) - 1
        return random.randint(range_start, range_end)


if __name__ == "__main__":
    main()