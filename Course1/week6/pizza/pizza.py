import sys
from tabulate import tabulate
import csv

def main():
    menu = []

    # Check if there is only 1 python file as an argument
    if len(sys.argv) == 2 and sys.argv[1][-4:] == ".csv":
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    menu.append
                    
                   

            print(f"{n_lines} non-commented lines")
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Usage: python script.py filename.py")

if __name__ == "__main__":
    main()
