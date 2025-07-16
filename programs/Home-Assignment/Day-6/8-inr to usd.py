# 🔹 Part D: Data Formatting + Return
# 8.	Currency Converter
# Function convert_to_usd(inr, rate=83.2) → converts INR to USD (default rate 83.2)

def convert_to_usd(inr, rate=83.2):
    usd = inr / rate
    return round(usd, 2)  
inr = 1000
usd = convert_to_usd(inr)
print(f"{inr} INR = {usd} USD")
