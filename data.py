#password strength checker program
def check_password_strength(password: str) -> str:
    if len(password) < 8:
        return "Weak"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if score <= 2:
        return "Weak"
    elif score <= 3:
        return "Medium"
    elif score <= 4:
        return "Strong"

password = input("Enter password: ")
print(check_password_strength(password))
