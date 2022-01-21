import pandas


alphabet_data = pandas.read_csv("Day26/NATO_Alphabet/nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}
user_input = input("Enter a word: ").upper()
print([nato_alphabet[letter] for letter in user_input])