import math

def are_collinear(points):

    collinear = False

    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    area = 1/2*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    if area == 0:
        collinear = True
    else:
        collinear = False
    return collinear

points = [(),(),()]

first_set = input("Enter the first set of coordinates, no spaces: ").strip('()').split(',')
points[0] = tuple(map(int,first_set))

second_set = input("Enter the second set of coordinates, no spaces: ").strip('()').split(',')
points[1] = tuple(map(int,second_set))

third_set = input("Enter the third set of coordinates, no spaces: ").strip('()').split(',')
points[2] = tuple(map(int,third_set))

result = are_collinear(points)
print(result)

