
def main():
    answer_to_everything = str(input("What is the meaning to life? ")).lower()
    if answer_check(answer_to_everything):
        print("yes")
    else: 
        print("no")

def answer_check(answer):
    return answer in ["42", "forty-two", "forty two"]

main()