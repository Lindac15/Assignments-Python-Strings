# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if len(first_name) < 2 or len(last_name) < 2:
    print("Error: First name and last name must be at least 2 characters long.")
else:
    print("Names are valid.")

# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

def check_password_complexity(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number."
    return "Password meets complexity requirements."

password = input("Enter your password: ")
print(check_password_complexity(password))

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format

def format_email(email):
    email = email.lower().strip()
    if "@" not in email:
        return "Invalid email address."
    return email

email = input("Enter your email address: ")
print(format_email(email))

