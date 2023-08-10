def main():
    while True:
        cart = []
        while True:
            try:
                item = str(input())
                if not item:
                    break
                cart.append(item)
            except KeyboardInterrupt:
                return_grocery_list(cart)
                return
            except EOFError:
                return_grocery_list(cart)
                return
        return
        

def return_grocery_list(grocery_list):
    # Iterate over all the items in the grocery list and make them lower case
    # and sort them in alphabetical order.
    sorted_grocery_list = sorted(grocery_list, key=lambda x: x.upper())
    unique_grocery_list = []
    for item in sorted_grocery_list:
        if item not in unique_grocery_list:
            print(f"{sorted_grocery_list.count(item)} {item}")
            unique_grocery_list.append(item)
        continue

if __name__ == "__main__":
    main()


    
