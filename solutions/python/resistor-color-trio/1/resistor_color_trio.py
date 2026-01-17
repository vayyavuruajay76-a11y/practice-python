def label(colors):
    color=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    total=int(str(color.index(colors[0]))+str(color.index(colors[1])))*(10**(color.index(colors[2])))
    if total>1000000000:
        return f"{total//1000000000} gigaohms"
    elif total>1000000:
        return f"{total//1000000} megaohms"
    elif total>1000:
        return f"{total//1000} kiloohms"
    else:
        return f"{total} ohms"
        
