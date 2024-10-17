import math

def calculate_slope(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    
    if y2-y1 == 0 or x2-x1 ==0:
        return 'Undefined'
    else:
        slope = (y2-y1)/(x2-x1)
        return slope
    
points = [(),()]

first_set = input("Enter first set of coordinates, no spaces: ").strip('()').split(',')
points[0] = tuple(map(int,first_set))

second_set = input("Enter second set of coordinates, no spaces: ").strip('()').split(',')
points[1] = tuple(map(int,second_set))

result = calculate_slope(points)
print(f"Slope: {result:.2f}")