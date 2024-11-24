class Student:
    def __init__(self, name = None, grade = 0):
        self.name = name
        self.grade = grade
    def is_passing(self):
        if self.grade >=65:
            return True
        else:
            return False
        
s1 = Student("Andrew", 64)
print(s1.is_passing())

s2 = Student("Rey", 100)
print(s2.is_passing())