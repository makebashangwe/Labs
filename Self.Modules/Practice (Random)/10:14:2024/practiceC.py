'''Challenge 1: Sum of Elements in a 1D List
Task: Write a function that takes a list of integers as an argument 
and returns the sum of all the elements in the list.'''

def calculate_sum(int_list):
    return(sum(int_list))
input_list = input("Enter A List: ")
int_list = []
int_list = list(map(int, input_list.split(",")))
result = calculate_sum(int_list)
print(result)