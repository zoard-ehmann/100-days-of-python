def add(*args):
    print(args[1])
    return sum(n for n in args)

print(add(1, 5, 3, 8))