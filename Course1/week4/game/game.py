import random
import sys

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                continue
            random_number = random.randint(1, n)
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            output = compare(random_number, guess)    
            print(output)

            if output == "You Win!":
                sys.exit()
        except ValueError:
            continue

def compare(random_number, guess):
    if guess == random_number:
        return "You Win!"
    elif guess > random_number:
        return "Too High!"
    else:
        return "Too Low!"

main()