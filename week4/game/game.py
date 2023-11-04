import random, sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            break
        except ValueError:
            pass
    while True:
        try:
            if level > 0:
                rndm = random.randint(1, level)
                guess = int(input("Guess: "))
                if guess == rndm:
                    sys.exit("Just right!")
                elif guess < rndm:
                    print("Too small!")
                elif guess > rndm:
                    print("Too large!")
            else:
                pass
        except ValueError:
            pass


main()