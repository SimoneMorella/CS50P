def main():
    expression = input("Expression: ")
    print(convert(expression))

def convert(expression):
    number1, operator, number2 = expression.split(" ")
    number1, number2 = float(number1), float(number2)
    match operator:
        case "+":
            return round(number1 + number2, 1)
        case "-":
            return round(number1-number2, 1)
        case "x" | "*":
            return round(number1 * number2, 1)
        case "/":
            return round(number1 / number2, 1)

main()
