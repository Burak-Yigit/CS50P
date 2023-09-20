import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    pass

data = response.json()
usd_rate_float = data["bpi"]["USD"]["rate_float"]
bitcoin_price = float(sys.argv[1]) * usd_rate_float
print(f"${bitcoin_price:,.4f}")