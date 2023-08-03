
def main():

    prompt = str(input("Give me a prompt: "))
    fillings = str(input("What do you want the spaces between the words to be? "))
    altered_prompt = replace_spaces_with(prompt, fillings)
    print(altered_prompt)

def replace_spaces_with(prompt, fillings):
    altered_prompt = prompt.replace(" ", fillings)
    return altered_prompt

main()