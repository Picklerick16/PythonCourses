import re
import sys


def main():
    if validate(input("IPv4 Address: ")):
        print("jezus")


def validate(ip):
    range = range(0,255)
    try: 
        first, second, third, fourth = str(ip).split(".")
        
    except:
        print("failled")


...


if __name__ == "__main__":
    main()