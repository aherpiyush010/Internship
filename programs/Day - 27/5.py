import requests

# Coordinates for a location (example: Nashik, India)
latitude = 19.9975
longitude = 73.7898

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    "&current=temperature_2m"
)

response = requests.get(url)
data = response.json()

temp = data["current"]["temperature_2m"]
print("Temperature:", temp, "°C")