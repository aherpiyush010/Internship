# Get a Random Dog Image
# API: https://dog.ceo/api/breeds/image/random
# Goal: Fetch and print the image URL (bonus: open it in the browser with webbrowser.open())

import requests
import webbrowser
url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)

image_url = response.json()["message"]
print(f"Dog Image URL: {image_url}")
webbrowser.open(image_url)