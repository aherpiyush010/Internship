# 9.	Email Generator
# Function generate_email(name, domain="example.com")
# •	Input: "John Doe" → Output: "john.doe@example.com"

def generate_email(name, domain=""):
    name = name.strip().replace(" ", ".")
    email = f"{name}@{domain}.com"
    return email

print(generate_email("Piyush aher", "gmail"))  

