def main():
    fruit = str(input("Item: "))
    give_facts_about(fruit)

def give_facts_about(fruit):
    # Data of the fruits
    fruits = [
        {"name": "apples", "calories": 130, "fat": 0, "proteins": 1},
        {"name": "avocados", "calories": 50, "fat": 4.5, "proteins": 1},
    ]

    for fr in fruits:
        # print the name, calories, fat, and proteins of the fruit
        if fr["name"] == fruit:
            print(f"Name: {fr['name']}")
            print(f"Calories: {fr['calories']}")
            print(f"Fat: {fr['fat']}")
            print(f"Proteins: {fr['proteins']}")
            return

    print(f"I don't know about {fruit}")

if __name__ == "__main__":
    main()