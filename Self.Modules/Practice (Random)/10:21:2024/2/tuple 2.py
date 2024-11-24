'''
Tuple Manipulation
Create a program that takes a tuple of mixed data types and counts 
how many elements are strings, integers, and floats. Return a 
dictionary with the counts. (Hint: Use type checking with isinstance.)
'''
'''
for i in range(len(list)):
    retrievev type
    if tyupe is Strings
    types[] = types + 1
'''
list_values = (1,"pretty",90,45,"poo", 0.2) #can change
types_values = {'strings': 0, 'integers': 0, 'floats': 0}
for i in range(len(list_values)):
    if isinstance(list_values[i],str):
        types_values['strings'] += 1
    elif isinstance(list_values[i],int):
        types_values['integers'] += 1
    elif isinstance(list_values[i],float):
        types_values['floats'] += 1
print(types_values)