def calculate_area(len,wid):
    if len < 0 or wid < 0:
        return "Invalid Input"
    else:
        return len * wid

print(calculate_area(1,4))