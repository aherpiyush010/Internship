import requests

API_KEY = 'YOUR_API_KEY'
city = 'Nashik'  
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
else:
    print(f"Error {response.status_code}: Failed to fetch weather data for {city}")
    