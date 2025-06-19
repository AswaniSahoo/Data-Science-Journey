def is_strong_pass(password):
    errors = [] #created an empty list and inserted every errors

    if len(password) < 8:
        errors.append("At least 8 characters required")
    if not any(char.isdigit() for char in password):
        errors.append("At least one digit required")
    if not any(char.isupper() for char in password):
        errors.append("At least one uppercase letter required")
    if not any(char.islower() for char in password):
        errors.append("At least one lowercase letter required")
    if not any(char in '!@#$%^&*()_+,./?><=][}{' for char in password):
        errors.append("At least one special character required")

    if errors:
        print("Password is Weak. Please fix:")
        for err in errors:
            print(f"- {err}")
    else:
        print("Password is Strong 🔒")

# Example tests
is_strong_pass("Aswani@G133")    # Strong
is_strong_pass("Aswani")         # Weak
is_strong_pass("aswani@123")     # Weak
