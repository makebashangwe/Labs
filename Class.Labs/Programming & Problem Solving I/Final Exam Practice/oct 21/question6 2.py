'''
Question 3: Write a program that prints all even numbers between 1 and 100 
but skips multiples of 10 using a for loop and the continue statement.

'''

for i in range(1,101):
    if i%2==0:  
        if i % 10 == 0:
            continue
        print(i)