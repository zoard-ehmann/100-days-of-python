student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 68, 98],
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(key)
    print(value)

# Looping through pandas DF
import pandas

student_df = pandas.DataFrame(student_dict)
print(student_df)

# Loop through columns
for (key, value) in student_df.items():
    print(key)
    print(value)
    
# Loop through rows
for (index, row) in student_df.iterrows():
    print(index)
    print(row.student)
    if row.student == "Angela":
        print(row.score)