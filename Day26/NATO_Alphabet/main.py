import pandas


alphabet_data = pandas.read_csv("Day26/NATO_Alphabet/nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

output = []
while len(output) == 0:
    user_input = input("Enter a word: ").upper()
    for letter in user_input:
        try:
            output.append(nato_alphabet[letter])
        except KeyError:
            print("Only US alphabet letters please.")
            output.clear()
            break

print(output)