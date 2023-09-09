import sys
import csv

def main():
    check_command_line_args()
    
    # try to open file
    try: 
        file = []
        with open(sys.argv[1], "r") as before_file:
            reader = csv.DictReader(before_file)
            for row in reader:
                last_name, first_name = row["name"].split(",")
                print(row)
                file.append({'first':first_name.lstrip(), "last":last_name, "house": row["house"]})

    except FileNotFoundError: 
        sys.exit(f"File named {sys.argv[1]} does not exist")

 
    with open(f"{sys.argv[2]}.csv" , "w", newline='') as after_file:
        writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for student in file:
            writer.writerow({"first":student["first"], "last": student["last"], "house":student["house"]}) 

def check_command_line_args():

    # Check if enought command-line-arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check if inputted file is a csv-file
    if not sys.argv[1][-4:] == ".csv":
        sys.exit(f"Could not read {sys.argv[1]}, not a csv-file")
    
    return

if __name__ == "__main__":
    main()

