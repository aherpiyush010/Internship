# Currency Converter
# API: https://api.exchangerate-api.com/v4/latest/USD
# Goal: Convert a given amount in INR to USD, EUR, etc. without functions

import requests
INR = 50
response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
data = response.json()

rates = data["rates"]["INR"]
USD = INR / rates
EUR = USD * data["rates"]["EUR"]

print(USD)
print(EUR)