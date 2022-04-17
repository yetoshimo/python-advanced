class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass

# For easy use, classes are populated in the same .py file

# Can be done with regex; however, for this code, it would be overkill


line = input()

valid_domains = ['com', 'bg', 'org', 'net']


while line != "End":

    if '@' in line:
        username, provider_domain = line.split('@')
        if len(username) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if provider_domain.split('.')[1] not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        # TODO - Can add provider (gmail, hotmail, abv, etc.) check < BUT NOT in the requirements
    else:
        raise MustContainAtSymbolError("Email must contain @")

    print('Email is valid')

    line = input()
