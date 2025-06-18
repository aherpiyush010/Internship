# 7.	Write a function get_min_max(numbers) that:
# o	Accepts a list
# o	Returns a tuple (min, max)
def get_min_max(numbers):

    if not numbers:
        
        print("List is empty ")
    
    min_value = min(numbers)
    max_value = max(numbers)
    print("Minimum value:", min_value)
    print("Maximum value:", max_value)
    return (min_value, max_value)
get_min_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])