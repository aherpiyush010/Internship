# 🔹 Part B: Math Logic
# 5.	Sum of Digits
# Function sum_of_digits(n) returns the sum of all digits in a number.
# Example: 123 → 6

def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10        
        total += digit        
        n = n // 10       
    print(total)   
    return total
sum_of_digits(12345)
