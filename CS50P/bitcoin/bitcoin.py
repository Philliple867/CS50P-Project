import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    url = "https://api.coincap.io/v2/assets/bitcoin"
    response = requests.get(url)
    data = response.json()

    price = float(data["data"]["priceUsd"])
    total = amount * price
    print(f"${total:,.4f}")
except:
    sys.exit()
