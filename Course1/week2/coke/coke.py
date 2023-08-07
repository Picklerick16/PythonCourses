def main():
    while True:
        total_inserted = 0

        while total_inserted < 50:
            coin = int(input("Insert a coin (25, 10, or 5 cents): "))

            if coin == 25 or coin == 10 or coin == 5:
                total_inserted += coin
                amount_due = 50 - total_inserted

                if amount_due > 0:
                    print(f"Amount due: {amount_due} cents")
                else:
                    change = -amount_due
                    print(f"You've inserted enough! Your change: {change} cents")
                    break
            else:
                print("Invalid coin. Please insert a valid coin.")

        choice = input("Do you want to buy another bottle? (yes/no): ")
        if choice.lower() != "yes":
            print("Thank you for using the Coca-Cola vending machine. Have a great day!")
            break

if __name__ == "__main__":
    main()