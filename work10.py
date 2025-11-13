from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        return 2025 - self.account_year

    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "Admin"
    
    def __str__(self):
        return f"{self.name} is an {self.get_role()} with an account age of {self.account_age()} years."

class Guest(User):
    def get_role(self):
        return "Guest"
    
    def __str__(self):
        return f"{self.name} is a {self.get_role()} with an account age of {self.account_age()} years."

a = Admin("Alice", 2020)
g = Guest("Bob", 2023)

print(a)
print(g)
