
def main():
    Call = str(input("Be quiet, what do you want to say? "))
    loweredCall = convert_to_indoor_voice(Call)
    print(loweredCall)

def convert_to_indoor_voice(toLower):
    loweredCall = toLower.lower()
    return loweredCall

main()
