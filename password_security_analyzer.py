import re

def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (use at least 12 characters).")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Symbols
    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    return score, feedback


def main():
    password = input("Enter a password to analyze: ")
    score, feedback = analyze_password(password)

    print("\nPassword Strength Score:", score, "/6")

    if score >= 5:
        print("Strong password 👍")
    elif score >= 3:
        print("Moderate password ⚠️")
    else:
        print("Weak password ❌")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print("-", tip)


if __name__ == "__main__":
    main()