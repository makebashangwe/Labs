def letterPositions(s1,s2):
    positions = []
    for index, char in enumerate(s1):
        if char == s2:
            positions.append(index)
            
    return tuple(positions)
    
s1 = input("Enter a phrase: ").lower()
s2 = input("Enter a letter: ").lower()
print(f"{s2} appears inside your phrase in the following positions: {letterPositions(s1,s2)}")