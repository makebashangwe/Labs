def convert_temp(temp,scale):
    if scale == "C":
        return (temp*9/5)+32 #fah
    elif scale == "F":
        return (temp-32)*5/9 #cel
    
print(convert_temp(scale = "C",temp = 32))