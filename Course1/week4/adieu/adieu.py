
def main():
    list_of_names = []
    
    while True:
        try:
            inputted_name = input("Name: ")
            if inputted_name == "":
                raise KeyboardInterrupt
            list_of_names.append(inputted_name)

        except KeyboardInterrupt:
            print("Adieu, adieu, to", end="")
            if len(list_of_names) == 1:
                print(f" {list_of_names[0]}")
            else:
                last_name = list_of_names[-1]
                other_names = ", ".join(list_of_names[:-1])
                print(f" {other_names}, and {last_name}")
            break  # Exit the loop and the program

main()
