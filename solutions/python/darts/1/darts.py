import math
def score(x, y):
    r=math.sqrt(x**2+y**2)
    if r<=10 and r>5:
        points=1
    elif r<=5 and r>1:
        points=5
    elif r<=1 and r>=0:
        points=10
    else:
        points=0

    return points
