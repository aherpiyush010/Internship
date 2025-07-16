import requests  # Import the requests library

# 1. Send a GET request to fetch all posts
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# 2. Print the response status code
print("Status Code:", response.status_code)

# 3. Print the first post in the response (in JSON format)
if response.status_code == 200:
    posts = response.json()  # Convert response to JSON
    print("First Post:")
    print(posts[0])  # Print the first post
else:
    print("Failed to fetch data.")
