#Email Validation System Using String Methods And Functions
def is_valid_email(email):
    # Check if the email contains exactly one '@' symbol
    if email.count('@') != 1:
        return False
    
    # Split the email into local and domain parts
    local_part, domain_part = email.split('@')
    
    # Check if the local part is not empty
    if not local_part:
        return False
    
    # Check if the domain part contains at least one '.' symbol
    if '.' not in domain_part:
        return False
    
    # Check if the domain part has a valid format (e.g., example.com)
    domain_parts = domain_part.split('.')
    if len(domain_parts) < 2 or any(not part for part in domain_parts):
        return False
    
    # Check for invalid characters in the local part
    invalid_chars = set(' !#$%^&*()+=[]{}|\\;:\'",<>/?`~')
    if any(char in invalid_chars for char in local_part):
        return False
    
    return True
# Main program
email = input("Enter email address: ")

if is_valid_email(email):
    print("Email is Valid")
else:
    print("Email is Invalid")