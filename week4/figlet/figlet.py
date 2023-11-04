import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    font_list = figlet.getFonts()
    valid = ["-f", "--font"]
    # figlet.setFont(font = 'dotmatrix')

    if len(sys.argv) == 1:
        rfont = random.choice(font_list)
        figlet.setFont(font = rfont)
        prompt = input("Input: ")
        print(figlet.renderText(prompt))

    elif len(sys.argv) == 3:
        if sys.argv[1] in valid and sys.argv[2] in font_list:
            figlet.setFont(font = sys.argv[2])
            prompt = input("Input: ")
            print(figlet.renderText(prompt))
        else:
           sys.exit("Insert valid arguments")

    else:
       sys.exit("Insert valid arguments")


main()