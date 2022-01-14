print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster.")
  if age < 12:
    print("The ticket will cost $5.00")
    bill = 5
  elif age <= 18:
    print("The ticket will cost $7.00")
    bill = 7
  elif age >= 45 and age <= 55:
    print("You have a midlife crisis, so you can ride for free.")
  else:
    print("The ticket will cost $12.00")
    bill = 12

  wants_photo = input("Do you want a photo? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Total bill: ${bill}.")

else:
  print("Sorry, you can't ride. :(")