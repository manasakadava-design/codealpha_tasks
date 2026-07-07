import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase letter")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add a number")

    if re.search(r"[!@#$%^&*]", password):
        strength += 1
    else:
        feedback.append("Add special character !@#$%^&*")

    if strength <= 2:
        result = "Weak"
    elif strength <= 4:
        result = "Medium"
    else:
        result = "Strong"

    return result, feedback

password = input("Enter your password: ")
result, feedback = check_password_strength(password)
print("Password Strength:", result)
if feedback:
    print("Suggestions:")
    for f in feedback:
        print("-", f)