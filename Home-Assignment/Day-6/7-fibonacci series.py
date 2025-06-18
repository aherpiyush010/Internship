
# 7.	Fibonacci Generator
# Function fibonacci(n) returns a list of first n Fibonacci numbers.
# Example: fibonacci(5) → [0, 1, 1, 2, 3]

def fibonacci(n):
    fib_series = []
    a = 0
    b = 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    
    return fib_series
print(fibonacci(5))
