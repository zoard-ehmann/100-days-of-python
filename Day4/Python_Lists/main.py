states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
print(states_of_america[-1])

states_of_america[1] = "Pencilvania"

states_of_america.append("Zoland")
states_of_america.extend(["Testland", "Macskaland"])

num_of_states = len(states_of_america)

print(states_of_america[num_of_states - 1])

fruits = ["Banana", "Apple", "Strawberry"]
vegetables = ["Kale", "Spinach"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)