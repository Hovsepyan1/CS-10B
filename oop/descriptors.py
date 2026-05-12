class StringValidator: #descriptor  __get__, __set__, __delete__
    def __set_name__(self, owner, name):
        print("__set_name__ caled...")
        print(name)
        self.name = name
    def __get__(self, instance, owner):
        # print(f"self = {self}")
        # print(f"instance = {instance}")
        # print(f"owner = {owner}")
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        print("__set__ called")
        if not isinstance(value, str):
            raise TypeError("Invalid Type!")
        if not value:
            raise ValueError("Invalid Value!")
        instance.__dict__[self.name] = value

class Person:
    name = StringValidator()
    surname = StringValidator()
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# p = Person("Yield", "Return")
# print()
# print(p.name, p.surname)
# print(Person.surname)

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    surname: str

p = Person(name="Yield", surname="Return")
print(p)