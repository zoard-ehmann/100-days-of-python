file = open("./Day24/Read_Write/my_file.txt")
contents = file.read()
print(contents)
file.close()


with open("./Day24/Read_Write/my_file.txt") as another_file:
    another_contents = another_file.read()
    print(another_contents)
    
    
with open("./Day24/Read_Write/new_file.txt", mode="a") as file:
    file.write("\nNew File.")