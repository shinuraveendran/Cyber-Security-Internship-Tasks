text = input("Enter message: ")
shift = int(input("Enter shift: "))

result = ""

for char in text:
    if char.isalpha():
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        result += char

print("Encrypted text:", result)
