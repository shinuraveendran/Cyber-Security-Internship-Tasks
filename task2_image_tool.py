from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]

            # Simple encryption (add key)
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print("Image Encrypted and saved as", output_path)


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]

            # Reverse operation
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print("Image Decrypted and saved as", output_path)


print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter choice: ")

input_path = input("Enter image file name (example: test.jpg): ")
output_path = input("Enter output file name: ")
key = int(input("Enter key (number): "))

if choice == "1":
    encrypt_image(input_path, output_path, key)
elif choice == "2":
    decrypt_image(input_path, output_path, key)
else:
    print("Invalid choice")
