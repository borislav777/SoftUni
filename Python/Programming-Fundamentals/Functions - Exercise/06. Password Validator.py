def password_is_valid(pasw):
    is_valid = True
    digit_counter = 0
    if len(pasw) < 6 or len(pasw) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not pasw.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    for el in pasw:
        if el.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    return is_valid


password = input()
result = password_is_valid(password)
if result:
    print("Password is valid")
