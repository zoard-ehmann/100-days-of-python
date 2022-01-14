#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator App!\n")

bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give?\n%")) / 100 + 1
people = int(input("How many people to split the bill?\n"))

calculation = bill * tip / people
print(f"Each person should pay ${calculation:.2f}")

# Same outcome with format function

# calculation = "{:.2f}".format(bill * tip / people)
# print(f"Each person should pay ${calculation}")