import re
import sys


def main():
 
    print(parse(input("HTML: ").strip()))

        


def parse(s):
    try: 
        matches = re.search(r"^https?://(www.)?youtube\.com/embed/.+\"$", s)
    except:
        sys.exit("no match")
    print(src)


...


if __name__ == "__main__":
    main()