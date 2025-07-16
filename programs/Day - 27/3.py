# List All Users from JSONPlaceholder
# API: https://jsonplaceholder.typicode.com/users
# Goal: Display names, emails, and company names of all users

import requests

users = requests.get("https://jsonplaceholder.typicode.com/users").json()
for i in users:
    print(f"Name: {i['name']}, Email: {i['email']}, Company: {i['company']['name']}")