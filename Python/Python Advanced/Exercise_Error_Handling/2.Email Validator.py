from email_validation import email_validation


email = input()

while not email == "End":
    if email_validation(email):
        print("Email is valid")
    email = input()
