alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(original_text, shift_number, operation):
    output = ""
    for char in original_text:
        if char in alphabet:
            if operation == 'decode':
                shift_number *= -1

            new_position = alphabet.index(char) + shift_number
            new_position %= len(alphabet)
            output += alphabet[new_position]
        else:
            output += char

    word = "encoded" if operation == "encode" else "decoded"
    print(f"The {word} text is {output}")

continue_program = "yes"
while continue_program == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if (direction not in ["encode", "decode"]):
        print("Invalid input")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)

    continue_program = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if (continue_program not in ["yes", "no"]):
        print("Invalid input")
        continue
