# 01. Person
class Person:
    def __init__(self, name: str, age: int):
        self.__age = age
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())

# 02. Email Validator
from re import split


class EmailValidator:
    __EMAIL_REGEX = '[@.]'

    def __init__(self, min_length: int, mails: list, domains: list):
        self.domains = domains
        self.mails = mails
        self.min_length = min_length

    def __validate_name(self, name):
        return self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        (name, mail, domain) = split(EmailValidator.__EMAIL_REGEX, email)
        return self.__validate_name(name) and self.__validate_mail(mail) and self.__validate_domain(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

# 03. Mammals
class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, type: str, sound: str):
        self.sound = sound
        self.type = type
        self.name = name

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())

# 04. Account
class Account:

    def __init__(self, id: int, balance: int, pin: int):
        self.__pin = pin
        self.__id = id
        self.balance = balance

    def __is_pin_valid(self, pin):
        return self.__pin == pin

    def get_id(self, pin: int):
        if not self.__is_pin_valid(pin):
            return f"Wrong pin"
        return self.__id

    def change_pin(self, old_pin: int, new_pin: int):
        if not self.__is_pin_valid(old_pin):
            return f"Wrong pin"
        self.__pin = new_pin
        return f"Pin changed"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
