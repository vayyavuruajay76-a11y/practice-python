def is_valid(isbn):
    fnstr = ''.join(e for e in isbn if e.isalnum()).lower()
    if len(fnstr)!=10:
        return False

    total=0

    for i in range(10):
        num=fnstr[i]

        if i<9:
            if not num.isdigit():
                return False
            val=int(num)
        else:
            if num.upper()=="X":
                val=10
            elif num.isdigit():
                val=int(num)
            else:
                return False

        total+=val*(10-i)

    return total%11==0
            
