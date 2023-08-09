def main():
    bill = add_item_to_bill("Item: ")
    print(f"Total: ${bill:.2f}")
def add_item_to_bill(food_item):
    while True:
        total = 0
        try: 
            while True:
                menu =  {
                    "Baja Taco": 4.00,
                    "Burrito": 7.50,
                    "Bowl": 8.50,
                    "Nachos": 11.00,
                    "Quesadilla": 8.50,
                    "Super Burrito": 8.50,
                    "Super Quesadilla": 9.50,
                    "Taco": 3.00,
                    "Tortilla Salad": 8.00
                }

                
                food = str(input(food_item)).title()
                total += menu[food]
                print(f"Total: ${total:.2f}")
        except KeyboardInterrupt:
            print("Ctrl+C pressed. Exiting...")
            break
        except KeyError:
            print(f"{food} is not a valid option. Please try again.")
        except ValueError:
            print(f"{food} is not a valid option. Please try again.")
    return total


if __name__ == "__main__":
    main()
