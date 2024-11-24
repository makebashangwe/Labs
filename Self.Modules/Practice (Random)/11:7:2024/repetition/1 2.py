''' Repetition Statements (while loops, for loops, break, continue)
Question:
Create a Python function print_even_numbers(n) that:

Prints even numbers from 0 up to, but not including, a given positive integer n.
Use a while loop in this function, and add a for loop version afterward.
Follow-Up: Try testing both with n = 10. Consider using break or continue if you think they’d make the loop clearer.
'''

def print_even(n):
    for i in range(1,n-1):
        if i % 2 ==0:
            print(i)
        else:
            continue

while True:
    try:
        n = int(input('Enter a number: '))
        break
    except ValueError:
        print("Enter a valid number.")

print_even(n)


#alternative method 

counter = 0
while counter != n:
    counter = counter + 1
    if counter % 2 == 0 and counter != n:
        print(counter)
    else:
        continue
