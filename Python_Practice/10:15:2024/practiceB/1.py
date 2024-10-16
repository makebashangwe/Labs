
width = int(input("Enter width: "))
height = int(input("Enter Height: "))

stars = '*'
spaces = ' '

for row in range(width): #top
    print(stars, end='')
print()
for row in range (height-2):
    print(stars,end='')
    for column in range(width-2):
        print(spaces, end='')
    print(stars)
    
   
for row in range(width): #bottom
    print(stars, end='')
print()




