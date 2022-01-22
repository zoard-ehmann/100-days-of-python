def add(*args):
    print(args[1])
    return sum(n for n in args)

print(add(1, 5, 3, 8))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        
my_car = Car(make="Nissan")
print(my_car.model)