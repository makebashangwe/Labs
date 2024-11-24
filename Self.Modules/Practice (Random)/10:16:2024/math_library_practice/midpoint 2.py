import math

def midpoint(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    
    x_midpoint = (x1+x2)/2
    y_midpoint = (y1+y2)/2
    midpoint = x_midpoint, y_midpoint
    return midpoint

points = [(),()]

first_set = input("Please input coordinates, no spaces: ").strip('()').split(',')
x1,y1 = map(int,first_set)
points[0] = x1,y1

second_set = input("Please input coordinates, no spaces: ").strip('()').split(',')
x2,y2 = map(int,second_set)
points[1] = x2,y2

answer = midpoint(points)
print(answer)

