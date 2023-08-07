
def main():

    normal_text = list(input("Input: "))
    omit_vowels(normal_text)

def omit_vowels(text):
    # Make a list of vowels to remove from the text
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for letter in text:
        # If the character is a vowel,
        if letter.lower() in vowels:
            # Remove it from the text
            text.remove(letter)
    # Convert the text back to a string   
    print("".join(text))

if __name__ == "__main__":
    main()