def resistor_label(colors):
    color=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    tolerance={"grey":"±0.05%","violet":"±0.1%","blue":"±0.25%","green":"±0.5%","brown":"±1%","red":"±2%","gold":"±5%","silver":"±10%"}
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"
    tole=tolerance[colors[-1]]
    if len(colors)==4:
        total=int(str(color.index(colors[0]))+str(color.index(colors[1])))*(10**(color.index(colors[2])))
    if len(colors)==5:
        total=int(str(color.index(colors[0]))+str(color.index(colors[1]))+str(color.index(colors[2])))*(10**(color.index(colors[3])))
    if total>=1000000000:
        val,units=total/1000000000,"gigaohms"
    elif total>=1000000:
        val,units=total/1000000,"megaohms"
    elif total>=1000:
        val,units=total/1000,"kiloohms"
    else:
        val,units=total,"ohms"
    if val==int(val):
        val=int(val)

    return f"{val} {units} {tole}"
