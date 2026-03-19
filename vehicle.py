# 🚗 Vehicle Management System
# 🎯 Նպատակ
# Ստեղծել տրանսպորտային միջոցների կառավարման համակարգ, որտեղ կարող ենք ստեղծել տարբեր տիպի մեքենաներ և կառավարել դրանք մեկ ընդհանուր համակարգում։
# Պետք է օգտագործել․
# ժառանգում (inheritance)
# մեթոդների վերասահմանում (method overriding)

# 1️⃣ Vehicle Class
# Ներկայացնում է ցանկացած տրանսպորտային միջոց։
# 📌 Ատրիբուտներ
# make
#  Տիպ՝ string
#  Արտադրող (օր․ "Toyota")
# model
#  Տիպ՝ string
#  Մոդել
# year
#  Տիպ՝ int
#  Թողարկման տարեթիվ

# 📌 Մեթոդներ
# description()
# Վերադարձնում է մեքենայի ամբողջական նկարագրությունը (string)
# age(current_year)
# Հաշվում է մեքենայի տարիքը
#  Վերադարձնում է → current_year - year
# 📌 Validation
# make, model → չեն կարող լինել դատարկ
# year → չի կարող լինել ապագայում
#  Սխալի դեպքում → raise ValueError

# 2️⃣ Car Class (Vehicle-ից ժառանգված)
# 📌 Լրացուցիչ ատրիբուտ
# number_of_doors (int)

# 📌 Մեթոդներ
# description()
# Վերագրել base class-ի մեթոդը և ավելացնել դռների քանակը

# 📌 Validation
# Դռների քանակը պետք է լինի > 0

from datetime import datetime

class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new):
        if not isinstance(new, str):
            raise TypeError("Invlaid type")
        if not new:
            raise ValueError("Invalid value")
        self.__make = new

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new):
        if not isinstance(new, str):
            raise TypeError("Invlaid type")
        if not new:
            raise ValueError("Invalid value")
        self.__model = new

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, new):
        if not isinstance(new, int):
            raise TypeError("Invalid Type")
        if new > datetime.now().year or new < 2018:
            raise ValueError("Invalid Value")
        self.__year = new

    def description(self):
        return f"Make - {self.make}\nModel - {self.model}\nYear-{self.year}"
    
    def age(self):
        return datetime.now().year - self.year
    

# a = Vehicle("Toyata", "Prado", 2025)
# print(a.description())
# print("Age - ", a.age())

class Car(Vehicle):
    def __init__(self, make : str, model : str, year : int, number_of_doors : int):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    @property
    def number_of_doors(self):
        return self.__number_of_doors
    
    @number_of_doors.setter
    def number_of_doors(self, new):
        if not isinstance(new, int):
            raise TypeError("Invalid Type")
        if new < 2 or new > 4:
            raise ValueError("Invalid Value")
        self.__number_of_doors = new

    def description(self):
        return "-------Car-------\n" + super().description() + f"\nNumber of doors - {self.number_of_doors}" + "\n-----------------"
    

c = Car("Toyata", "Camry", 2026, 4)
print(c.description())


class Fleet:
    def __init__(self):
        self.vehicles = []

    def 