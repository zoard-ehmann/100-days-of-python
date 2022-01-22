def add(*args):
    print(args[1])
    return sum(n for n in args)

print(add(1, 5, 3, 8))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)