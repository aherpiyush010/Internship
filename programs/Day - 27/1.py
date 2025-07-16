# Task:
# Get a Random Joke
# API: https://official-joke-api.appspot.com/random_joke
# Goal: Fetch and display the joke setup and punchline.

import requests 
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
if response.status_code == 200:
    joke = response.json()
    print(f"Setup: {joke['setup']}")
else:
    print("Error:", response.status_code)
    

    
    