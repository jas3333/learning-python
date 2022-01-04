alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(text, move, choice):
    coded_message = ""
    if choice == "decode":
        move *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            print(f"Position: {position} -- {char} -- ")
            new_position = (position + move) % len(alphabet)
            print(f"New_position: {new_position} --")
            coded_message += alphabet[new_position]
        else:
            coded_message += char
    return coded_message

choose = input("Encode or decode a message?\n")
message = input("Input your message.\n")
shift = int(input("Enter the shift amount.\n"))

new_message = ceasar(message, shift, choose)
print(f"Your message reads: {new_message}")


