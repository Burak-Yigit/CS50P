from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()
my_font = random.choice(font_list)

if len(sys.argv) < 2:
    figlet.setFont(font=my_font)
    print("Output:\n "+figlet.renderText(input("Input: ")))
elif len(sys.argv) < 3:
    sys.exit("Invalid Usage")
elif len(sys.argv) < 4:
    if sys.argv[1] != "-f" and sys.argv[1] != "-font":
        sys.exit("Invalid Usage")
    else:
        if sys.argv[2] in font_list:
            figlet.setFont(font=sys.argv[2])
            print("Output:\n "+figlet.renderText(input("Input: ")))
        else:
            sys.exit("Invalid Usage")