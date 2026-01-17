def color_code(color):
    codes=[x for x in range(0,10)]
    code_map=dict(zip(colors(),codes))
    return code_map[color]
    


def colors():
    colorr=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    return colorr
