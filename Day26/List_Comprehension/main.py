import random

numbers = [1, 2, 3]
new_numbers = [number + 1 for number in numbers]
print(new_numbers)

name = "Zoard"
name_list = [letter for letter in name]
print(name_list)

doubles = [num * 2 for num in range(1, 5)]
print(doubles)
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

new_names = [name for name in names if len(name) <= 4]

cap_names = [name.upper() for name in names if len(name) >= 5]

student_scores = {student:random.randint(1, 100) for student in names}

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}