
def main():
    if validate(input("IPv4 Address: ")):
        print("Valid")
    else:
        print("invalid")

def validate(ip):
    try: 
        list_numbers = str(ip).split(".")
        for num in list_num:
            if not num in range(255):
                return False
        return True
    except:
        print("invalid")


if __name__ == "__main__":
    main()