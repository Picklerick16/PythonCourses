
def main():
    expression = list(input("Expression: "))
    print(expression)
    print(interprete(expression))

def interprete(to_calculate):
    num_to_add = 0

    while "+" in to_calculate:
        
        index = to_calculate.index("+")
        num_to_add = (int(to_calculate[index+1]) + int(to_calculate[index-1]))

        print(num_to_add)
        to_calculate[index - 1 : index + 2] = [num_to_add]
        print(to_calculate)
        
    '''
    if "-" in to_calculate:
        index = to_calculate.index("-")
        answer += (to_calculate[index+1] - to_calculate[index-1])
    '''
    return num_to_add

main()