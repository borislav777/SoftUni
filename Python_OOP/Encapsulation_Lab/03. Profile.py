class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.pass_length(value) and self.pass_have_digits(value) and self.pass_have_uppercase(value):
            self.__password = value

        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def pass_length(self, password):
        if len(password) >= 8:
            return True
        return False

    def pass_have_digits(self, password):
        digit = [d for d in password if d.isdigit()]
        if digit:
            return True
        return False

    def pass_have_uppercase(self, password):
        uppercase = [u for u in password if u.isupper()]
        if uppercase:
            return True
        return False

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

