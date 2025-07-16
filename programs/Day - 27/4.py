import requests

lat = 19.9975
lon = 73.7898

url = "https://api.open-meteo.com/v1/forecast"f"?latitude={lat}&longitude={lon}""&current=temperature_2m"


response = requests.get(url)
data = response.json()

temp = data["current"]["temperature_2m"]
print("Temperature:", temp, "°C")

if temp > 30:
    print("It’s hot!")
if temp < 15:
    print("It’s cold!")
    
    
    
    
    