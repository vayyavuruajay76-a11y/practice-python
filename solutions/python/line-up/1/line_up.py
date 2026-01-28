def line_up(name, number):
    if number==11or number==12 or number==13 or number%100==12:
        return f"{name}, you are the {number}th customer we serve today. Thank you!"
    elif number%10==1:
        return f"{name}, you are the {number}st customer we serve today. Thank you!"
    elif number%10==2:
        return f"{name}, you are the {number}nd customer we serve today. Thank you!"
    elif number%10==3:
        return f"{name}, you are the {number}rd customer we serve today. Thank you!"
    else:
        return f"{name}, you are the {number}th customer we serve today. Thank you!"
