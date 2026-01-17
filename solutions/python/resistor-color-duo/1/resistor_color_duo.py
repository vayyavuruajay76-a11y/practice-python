def value(colors):
    color=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    value=''
    for x in colors[:2]:
        value+=str(color.index(x))
    return int(value)
