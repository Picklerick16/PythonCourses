import sys
import requests
import json

def main():

    try:
        if len(sys.argv) == 2:
            amount_to_buy = float(sys.argv[1])
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            o = response.json()
            value = o['bpi']['USD']['rate_float']
            print (f"That is about {round(amount_to_buy * value, 2)} USD")	
 
        sys.exit()
    except ValueError:
        sys.exit("Invalid amount to buy")

    except requests.RequestException:
        print("Connection error")
        sys.exit()
if __name__ == "__main__":
    main()