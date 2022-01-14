import random

# Importing and using a custom module

# import my_module
# print(my_module.pi)

random_integer = random.randint(1, 10)
print(random_integer)

# 0.0000000 - 0.9999999...
random_float = random.random()
print(random_float)

# 0.00000... - 4.99999...
random_float * 5

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")