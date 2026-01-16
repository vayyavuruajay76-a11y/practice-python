def is_armstrong_number(number):
    strnumber=str(number)
    c=0
    for value in strnumber:
        b=len(strnumber)
        a=int(value)
        c+=a**b

    if c==number:
        return True
    else:
        return False
