# 6.	Armstrong Number Checker
# Function is_armstrong(n) returns True if number is an Armstrong number.
# (e.g., 153 → 1³ + 5³ + 3³ = 153)
def is_armstrong(n):
    total = 0
    temp = n
    num_digits = len(str(n))
    
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    print(total)
    if total == n:
        return True
    else:
        return False

is_armstrong(765)
