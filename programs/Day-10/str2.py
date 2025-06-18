def string_to_dict(input_string):
    # Create an empty dictionary
    result = {}
    
    # Split the string by commas to separate key-value pairs
    pairs = input_string.split(',')
    
    for pair in pairs:
        # Split each pair by colon to get key and value
        if ':' in pair:
            key, value = pair.split(':', 1)
            result[key.strip()] = value.strip()
        else:
            print(f"Skipping invalid pair: {pair}")
    
    return result

# Example usage
input_str = "name:John, age:30, city:New York"
converted_dict = string_to_dict(input_str)
print("Converted Dictionary:", converted_dict)
