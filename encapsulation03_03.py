# class Person:
#     def __init__(self, name, surname, age, email="a@gmail.com"):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.email = email
#     def __str__(self):
#         return f"Person  \nname - {self.name}\nsurname - {self.surname}\nage - {self.age}"
    
#     def __repr__(self):
#         return f"__repr__ called..."

# p = Person("James", "Jamshoyan", 56)
# # print(p.__repr__())
# print(p.__dict__)
# print(globals())

# encapsulation
#private public
# class Person:
#     def __init__(self, name):   #constructor
#         self.set_name(name)

#     def get_name(self): #selector / getter
#         return self.__name
    
#     def set_name(self, new_name): #mutator / setter mutate = poxel
#         if not isinstance(new_name, str):
#             raise TypeError("Invalid Type")
#         if not new_name:
#             raise ValueError("Invalid Value")
#         self.__name = new_name

#     name = property(get_name, set_name)
# p = Person("Edik")
# # print(p.get_name())
# # p.set_name("Xeloq mna")
# # print(p.get_name())

# print(p.name)
# p.name = "Vardges"
# print(p.name)


# Ստեղծել Student class․
# Ատրիբուտներ և մեթոդներ՝
# private __grade
# set_grade(value) → grade-ը պետք է լինի 0–100 միջակայքում
# get_grade()
# Եթե սխալ արժեք է տրվում → տպի "Invalid grade"


# class Student:
#     def __init__(self,grade):
#         self.grade=grade

#     def set_grade(self,new_grade):
#         if not isinstance(new_grade,int):
#             raise TypeError("Invalid Type")
#         if new_grade<0 or new_grade>100:
#             raise ValueError("Invalid Value")
#         self.__grade=new_grade
#     def get_grade(self):
#         return self.__grade
#     grade=property(get_grade,set_grade)

# usanox=Student(100)
# print(usanox.grade)
# usanox.grade=70
# print(usanox.grade)




# class Student:
#     def __init__(self, grade):
#         self.grade = grade

#     @property
#     def grade(self):
#         return self.__grade
    
#     @grade.setter
#     def grade(self, new_grade):
#         if not isinstance(new_grade , int):
#             raise TypeError("Invalid Type")
#         if new_grade < 0 or new_grade > 100:
#             raise ValueError("Invalid Value")
#         self.__grade = new_grade
    

# usanox = Student(10)
# print(usanox.grade)
# usanoxuhi = Student(23)
# print(usanoxuhi.grade)
# usanoxuhi.grade = "text"








# Ստեղծել Temperature class․
# Ատրիբուտներ և մեթոդներ՝
# private __celsius
# մեթոդ՝ set_temperature(value)
# temperature-ը չպետք է լինի < -273 (absolute zero)
# to_fahrenheit() մեթոդ


class Temperature:
    def __init__(self, temperature):
        self.celsius = temperature
    
    def set_temperature(self, value):
        if value < -237:
            raise ValueError("Absolute Zero temperature")
        self.celsius = value
    
    def to_farenheit(self):
        farenheit = (self.celsius * 1.8) + 32

paraqar = Temperature(-2333)
print(paraqar.celsius)
paraqar_hamaynq = Temperature(123)
print(paraqar_hamaynq.celsius)
#comment