alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_count = len(alphabet)

continue_program = "yes"
while continue_program == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if(direction not in ["encode", "decode"]):
        print("Invalid input")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    direction(text, shift)

    continue_program = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if(continue_program not in ["yes", "no"]):
        print("Invalid input")
        continue


def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            new_position = (alphabet.index(char) + shift) % alphabet_count
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char

    print(f"The encoded text is {encrypted_text}")


# encrypt(text, shift)