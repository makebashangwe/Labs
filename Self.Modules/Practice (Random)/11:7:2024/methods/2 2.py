def greet_user(name = None, age = None):
    if name is not None and age is not None:
        print(f"Hello, {name.capitalize()}! You are {age} years old!")
    elif name is not None:
        print(f"Hello, {name.capitalize()}!")
    else:
        print("Hello!")

greet_user("alice")
greet_user('demarus', 25)
greet_user()