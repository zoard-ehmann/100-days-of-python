# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("Howdy?")
    print("Isn't the weather nice today?")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Howdy, {name}?")

greet_with_name("Zoard")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Zoard", "Hungary")
greet_with(location = "Budapest", name = "János")