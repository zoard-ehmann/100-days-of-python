alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(text, shift, direction):
    processed_text = ""
    for char in text:
        if char in alphabet:
            if direction == "encode":
                processed_text += alphabet[alphabet.index(char) + shift]
            elif direction == "decode":
                processed_text += alphabet[alphabet.index(char) - shift]
        else:
            processed_text += char
    print(f"Result: {processed_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

run = True

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        prompt = input("Another run? Y or N\n").lower()
        if prompt == "n":
            run = False
    else:
        print("Invalid direction")