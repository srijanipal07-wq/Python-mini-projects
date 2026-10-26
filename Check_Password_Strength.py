# Check Password Strength
password = input("Enter a password to check its strength: ")

# Define criteria for a strong password
min_length = 8
has_lowercase = False
has_uppercase = False
has_digit = False
has_special = False

# Define special characters
special_characters = "!@#$%^&*()-+"

# Check each character in the password
for char in password:
    if char.islower():
        has_lowercase = True
    if char.isupper():
        has_uppercase = True
    if char.isdigit():
        has_digit = True
    if char in special_characters:
        has_special = True

# Evaluate the strength of the password
if len(password) >= min_length and has_lowercase and has_uppercase and has_digit and has_special:
    print("The password is strong.")
else:
    print("The password is not strong enough.")