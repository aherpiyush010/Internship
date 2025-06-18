# 10-	Password Masker
# Function mask_password(password) returns a masked version
# Example: "secret" → "******"

def mask_password(password):
    return '*' * len(password)
print(mask_password("secret"))  
