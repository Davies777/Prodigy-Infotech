import re

def assess_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    # Calculate score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback based on score
    if score == 5:
        strength = "Very Strong"
        feedback = "Your password is very strong."
    elif score == 4:
        strength = "Strong"
        feedback = "Your password is strong but could be improved with more special characters or numbers."
    elif score == 3:
        strength = "Moderate"
        feedback = "Your password is moderate. Consider adding uppercase letters, numbers, or special characters."
    elif score == 2:
        strength = "Weak"
        feedback = "Your password is weak. Consider adding uppercase letters, numbers, and special characters."
    else:
        strength = "Very Weak"
        feedback = "Your password is very weak. It should be at least 8 characters long and include uppercase letters, lowercase letters, numbers, and special characters."

    return strength, feedback

# Example usage
password = input("Enter your password to check its strength: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
print(f"Feedback: {feedback}")
