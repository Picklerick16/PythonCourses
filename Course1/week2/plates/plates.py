def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if plate is between 2 and 6 characters long
    if 1 < len(s) <= 6:
        # Check if first and second characters are letters
        if not (s[0].isalpha() and s[1].isalpha()):
            return False
        
        # Check if all characters after the second letter are digits
        for ch in s[2:]:
            if not ch.isdigit():
                return False
        return True

    return False


main()