from custom_errors import NameTooShortError, MustContainAtSymbolError,InvalidDomainError


def email_validation(email):
    valid_domains = ('com', 'bg', 'net', 'org')
    try:
        username, domain = email.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    try:
        name, extension = domain.split('.')
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if extension not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    return True
