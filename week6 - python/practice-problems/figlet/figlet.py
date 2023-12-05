from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font="big")
    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))
    sys.exit(0)
elif len(sys.argv) == 3:
    args = sys.argv[1:]
    if args[0] == "-f" or args[0] == "--font":
        font = args[1]
        if font in fonts:
            figlet.setFont(font=font)
            text = input("Input: ")
            print("Output:")
            print(figlet.renderText(text))
            sys.exit(0)
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)
