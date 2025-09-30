# ===== TASK 2: Email Validator =====
# Create a custom InvalidEmailError exception
# The function should validate email format and raise InvalidEmailError if:
# - Email doesn't contain exactly one '@' symbol
# - Email doesn't contain at least one '.' after the '@'
# If input is empty, raise ValueError with message "Error: email cannot be empty"
# Keep asking until a valid email is entered

print("=== Task 2: Email Validator ===")
print("Email must contain '@' and a domain with '.'\n")

class InvalidEmailError(Exception):
    pass

def validate_email(prompt):
    valid = False
    while not valid:
        email = input(prompt)
        if email == "":
            print("Error: email cannot be empty")
            continue
        if email.count('@') != 1:
            print("Email must contain exactly one '@'")
            continue
        at_position = email.find('@')
        after_atsign = email[at_position + 1:]
        if '.' not in after_atsign:
            print("Email must contain '.' after '@'")
            continue
        
        valid = True
    
    return email

email = validate_email("Enter your email: ")
print(f"Email accepted: {email}")
print()

