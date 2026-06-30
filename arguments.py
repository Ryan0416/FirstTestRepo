#函式預設引數(Default arguments)

def greet(name, greeting="Hello"):
    name = input("what is your name? ")
    print(f"{greeting} {name}!")

greet("", "glacias")
