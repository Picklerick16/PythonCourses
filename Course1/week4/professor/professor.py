import random


def main():

    # Set number of levels
    levels = [1,2,3]
    completely_finished = False
    is_valid_level = False

    # Check if level inputted is valid
    while not is_valid_level:
        n = get_level()
        if n not in levels:
            continue
        else:
            is_valid_level = True

    number_of_solved_problems = 0
    number_of_problems_left = 10
    number_of_problems = 10
    while not completely_finished:
            
        X, Y = generate_integers(n)
        reset = False
        answer = X + Y
        wrong_in_a_row = 0
        while not reset:
            try: 
                user_answer = int(input(f"{X} + {Y} = "))

                # If user answer is not correct
                if not user_answer == answer:
                    print("EEE")
                    wrong_in_a_row += 1
                
                # If wrong 3 times in a row
                if wrong_in_a_row == 3:
                    print(f"Correct answer: {answer}")
                    number_of_solved_problems -= 1
                    break

                # If user answer is correct
                elif user_answer == answer:
                    number_of_solved_problems += 1
                    number_of_problems_left -= 1
                    reset = True
            
            except ValueError:
                continue

        if number_of_problems_left == 0:
            print(f"Scored {number_of_solved_problems} out of {number_of_problems}")
            completely_finished = True
    
def get_level():
    return int(input("Level:"))


def generate_integers(level):

    x = random.randint(1, 10 ** level)
    y = random.randint(1, 10 ** level)
    return x, y


if __name__ == "__main__":
    main()