
def main():

    prompt = str(input("Hello, which smiley do you wish to convert? "))
    print(convert_emoji(prompt))

def convert_emoji(prompt):
    # convert emoji 
    converted_emoji = prompt.replace(":)", "🙂").replace(":(", "☹")
    return converted_emoji

main()
