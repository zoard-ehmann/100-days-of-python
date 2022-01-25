# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Catching exceptions
# try:
#     file = open("Day30/Exceptions/a_file.txt")
#     a_dictionary = {"key": "value"}
#     value = a_dictionary["key"]
# except FileNotFoundError:
#     file = open("Day30/Exceptions/a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # Raising an exception
#     raise TypeError("This is a fictional error.")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
