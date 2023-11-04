def main():
    coins = [25, 10, 5]
    cost = 50
    while cost > 0:
        print("Amount Due:", cost)
        money = int(input("Insert Coin: "))
        if money in coins:
            cost -= money
            if cost <= 0:
                print("Change Owed:", cost * -1)
                break
            else:
                continue
        else:
            continue

main()