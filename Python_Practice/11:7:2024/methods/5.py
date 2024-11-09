def add (n2, n1):
    return n1 + n2


call = 0
          
for i in range(5):
    n1 = 1
    n2 = 1
    print(add(n1,n2), end=" ")
    call += 1

print()
print(f"There were {call} calls to this function")
