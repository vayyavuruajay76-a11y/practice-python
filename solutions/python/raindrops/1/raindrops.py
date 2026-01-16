def convert(number):
    result = ""
    
    # Check divisibility and append corresponding sounds
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
        
    # If no sounds were added, return the number as a string
    return result or str(number)