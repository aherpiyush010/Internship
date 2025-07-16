import requests

# API endpoint for posts
url = "https://jsonplaceholder.typicode.com/posts"

# JSON payload to send
payload = {
    "title": "New Post",
    "body": "This is a test post.",
    "userId": 1
}

# 1. Send POST request with JSON payload
response = requests.post(url, json=payload)

# 2. Parse and print the response JSON (new post with ID)
if response.status_code == 201:  # 201 Created
    new_post = response.json()
    print("New Post:", new_post)
else:
    print("Failed to create a new post. Status Code:", response.status_code)
