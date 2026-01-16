def equilateral(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if a!=0 and b!=0 and c!=0 and a+b>=c and b+c>=a and c+a>=b:
        return True if a==b and b==c and c==a else False
    else:
        return False
    


def isosceles(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if a!=0 and b!=0 and c!=0 and a+b>=c and b+c>=a and c+a>=b:
        return True if a==b or b==c or c==a else False
    else:
        return False
    
    


def scalene(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if a!=0 and b!=0 and c!=0 and a+b>=c and b+c>=a and c+a>=b:
        return True if a!=b and b!=c and c!=a else False
    else:
        return False
