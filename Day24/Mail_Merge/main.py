#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"


with open("./Day24/Mail_Merge/Input/Names/invited_names.txt") as names:
    names = names.readlines()


with open("./Day24/Mail_Merge/Input/Letters/starting_letter.txt") as template:
    letter = template.read()


for name in names:
    sanitized_name = name.strip()
    with open(f"./Day24/Mail_Merge/Output/ReadyToSend/letter_to_{sanitized_name}.txt", mode="w") as to_send:
        to_send.write(letter.replace(PLACEHOLDER, sanitized_name))
