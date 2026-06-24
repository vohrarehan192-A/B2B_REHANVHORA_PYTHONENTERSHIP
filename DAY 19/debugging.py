# BUGGY CODE:
"""
def calculate_total(string_list)
    total = 0
    for item in string_list:
        try
            num = int(item)
            total + num
        except ValueError
            print(f"Skipping invalid item: {item}")
    
    return total

data = ["10", "20", "apple", "30"]
result = calculate_total(data)
print("Total Sum = " + result)
"""

# FIXED CODE:

def calculate_total(string_list): # Fix 1: Added missing colon
    total = 0
    for item in string_list:
        try: # Fix 2: Added missing colon
            num = int(item)
            total += num # Fix 3: Logic error (was total + num, not saving the result)
        except ValueError: # Fix 4: Added missing colon
            print(f"Skipping invalid item: {item}")
    
    return total

data = ["10", "20", "apple", "30"]
result = calculate_total(data)
print(f"Total Sum = {result}") # Fix 5: Used f-string instead of string concatenation with integer
