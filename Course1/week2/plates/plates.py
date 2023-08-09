def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if plate has at least 3 characters
    if 2 <= len(s) <= 6:
        # Check if first and second characters are letters
        if s[0].isalpha() and s[1].isalpha():
            # Check if all characters after the second character are digits
            for ch in s[2:]:
                if ch.isdigit():
                    index = s.index(ch)
                    for end_character in s[index:]:
                        if not end_character.isdigit():
                            return False
                    return True
            return False  # No digits found after the second character
        
    return False


main()