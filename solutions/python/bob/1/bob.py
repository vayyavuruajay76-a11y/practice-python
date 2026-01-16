def response(hey_bob):
    message = hey_bob.strip()
    
    # Check for silence (empty after stripping)
    if not message:
        return "Fine. Be that way!"
    
    # Check if it's a yelled question (all caps and ends with ?)
    if message.isupper() and message.endswith('?'):
        return "Calm down, I know what I'm doing!"
    
    # Check if it's yelling (all caps)
    if message.isupper():
        return "Whoa, chill out!"
    
    # Check if it's a question (ends with ?)
    if message.endswith('?'):
        return "Sure."
    
    # Anything else
    return "Whatever."