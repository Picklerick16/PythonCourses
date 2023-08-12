import sys
import pyfiglet as figlet
import random

def main():
    if len(sys.argv) == 1:
        is_random_font = True
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font" or sys.argv[1] == "-"):
        is_random_font = False
    else:
        sys.exit()

    prompt = input("Enter text: ")
    converted_text = convert_text(prompt, is_random_font)
    print(converted_text)

def convert_text(text, is_random_font):
    if is_random_font:
        random_font_name = random.choice(figlet.FigletFont.getFonts())
        chosen_font = figlet.Figlet(font=random_font_name)
        return chosen_font.renderText(text)
    else:
        chosen_font = figlet.Figlet(font=sys.argv[2])
        return chosen_font.renderText(text)

if __name__ == "__main__":
    main()
