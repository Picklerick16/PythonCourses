
def main():
    camel_case = list(input("Camelcase: "))
    print(convert(camel_case))


def convert(camel):
    
    for letter in camel:
        if letter.islower() == True:
            continue
        
        else:
            index = camel.index(letter)
            camel[index] = "_" + letter.lower()

    return "".join(camel)

main()


            

        

