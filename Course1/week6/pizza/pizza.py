import sys

def main():
    n_lines = 0

    # Check if there is only 1 python file as an argument
    if len(sys.argv) > 1 and sys.argv[1][-3:] == ".py":
        try:
            with open(sys.argv[1], 'r') as file:
                lines = file.readlines()
                
                for line in lines:
                    # Remove leading and trailing whitespace
                    line = line.strip()
                    
                    # Ignore commented lines
                    if line and not line.startswith("#"):
                        n_lines += 1

            print(f"{n_lines} non-commented lines")
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Usage: python script.py filename.py")

if __name__ == "__main__":
    main()
