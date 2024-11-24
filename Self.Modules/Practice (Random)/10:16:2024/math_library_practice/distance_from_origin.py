import math

def distance_from_origin(points):
    x = points[0]
    y = points[1]

    d = math.sqrt((x**2)+(y**2))
    return d

coordinates = input("Enter coordinates, no spaces: ").strip('()').split(',')
points = list(map(int,coordinates))

result = distance_from_origin(points)
print(result)
