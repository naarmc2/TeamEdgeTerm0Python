import random

# Define sets of characters for different password categories
lowercase_letters = "abcdefghijklmnopqrstuvwx"
uppercase_letters = lowercase_letters.upper()
digits = "1234567890"
symbols = "!$?@#%^&*()_+-=ƒ∂ßåœ∑´®®†¥¨ˆøπ¬˚∆˙˙©∂ßßå≈ç√∫˜µ"

# Combine all character sets
all_chars = lowercase_letters + uppercase_letters + digits + symbols

# Set password length
password_length=100

# Generate a random password
password = "".join(random.sample(all_chars, password_length))

# Print the generated password
print(password)
