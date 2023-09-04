def main():
    students = [{
        "name":"weasley"},
        {"name": "Potter"}
    ]

    for student in sorted(students, key=lambda stud: stud["name"]):
        print(student["name"])

if __name__ == "__main__":
    main()