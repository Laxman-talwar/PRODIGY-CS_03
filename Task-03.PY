import re

def check_password_complexity(password):
    # Define the complexity rules
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @#$%^&*()_+!]", password) is None

    # Calculate the overall validity
    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    # Collect the error messages
    errors = {
        'length_error': length_error,
        'digit_error': digit_error,
        'uppercase_error': uppercase_error,
        'lowercase_error': lowercase_error,
        'symbol_error': symbol_error
    }

    return password_ok, errors

def print_password_complexity_results(password):
    password_ok, errors = check_password_complexity(password)
    
    if password_ok:
        print("Password is strong.")
    else:
        print("Password is not strong enough.")
        if errors['length_error']:
            print(" - Password must be at least 8 characters long.")
        if errors['digit_error']:
            print(" - Password must contain at least one digit.")
        if errors['uppercase_error']:
            print(" - Password must contain at least one uppercase letter.")
        if errors['lowercase_error']:
            print(" - Password must contain at least one lowercase letter.")
        if errors['symbol_error']:
            print(" - Password must contain at least one special character (@, #, $, etc.).")

# Example usage
password = input("Enter a password to check its complexity: ")
print_password_complexity_results(password)
