
def main():

    greeting = str(input("Greeting: ")).lower()

    print(check_originality(greeting))

def check_originality(reply):
    match reply:
        case "hello":
            return "$0"
        #case is set to reply if h is in reply
        # is case is reply match is case and condition is fulfilled
        # to return the value
        case reply if "h" in reply:
            return "$20"
        case _:
            return "$100"

main()