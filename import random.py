import random
import string

# Ask the user for the length of the password
length = int(input("Enter the desired password length: "))

# Define characters to use in the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_chars = letters + digits + symbols

# Generate password
password = ''.join(random.choice(all_chars) for i in range(length))

# Show the password
print("Generated Password:", password)
