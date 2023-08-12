import emoji

def main():
    print(convert_to_emoji("Emoji: "))
    
def convert_to_emoji(emoji_string):
    # Ask for the user to input a string to convert to emoji
    # Convert the input string to emoji
    return emoji.emojize(f"Python is {input(emoji_string)}")

if __name__ == "__main__":
    main()