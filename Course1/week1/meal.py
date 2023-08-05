def main():
    prompted_time = list(input("What time is it? "))
    converted_time = convert(prompted_time)
    match converted_time:
        case converted_time if 19 >= converted_time > 18:
            print("dinner")
        case converted_time if 13 >= converted_time > 12:
            print("lunch")
        case converted_time if 8 >= converted_time > 7:
            print("breakfast")
        case _:
            print("no time to eat yet!")

def convert(time):
    if ":" in time:
        index = time.index(":")
        hours = int("".join(time[:index]))
        minutes = int("".join(time[index + 1:]))    
        # turn prompted time into a float
        converted_time = float(f"{hours}.{int(minutes/0.6)} ")
        return converted_time

    return 


if __name__ == "__main__":
    main()
