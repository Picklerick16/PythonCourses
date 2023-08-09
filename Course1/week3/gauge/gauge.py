def main():
    fraction = fuel_left("Fraction: ")
    print(fraction)

def fuel_left(prompt):
    while True:
        try: 
            fraction = list(input(prompt))
            # Find the index of the "/" in the fraction
            position_divide_sign = fraction.index("/")
            # Take the left side as the numerator
            numerator = int("".join(fraction[:position_divide_sign]))
            # Take the right side as the denominator
            denominator = int("".join(fraction[position_divide_sign + 1:]))
            # Calculate the percentage
            percentage = (numerator / denominator) * 100
            
            if percentage >= 99:
                return "F"

            elif percentage <= 1:
                return "E"
        
            return str(round(percentage))+"%"

        except ValueError:
            print("Please enter a valid number.")
            continue
        except ZeroDivisionError:
            print("Please don't divide by zero.")
            continue

if __name__ == "__main__":
    main()