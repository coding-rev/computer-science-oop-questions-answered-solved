#Question 2
# 2A
class Pet:
    def __init__(self):
        self.__name         = "Default Pet name"          
        self.__animal_type  = "Default Animal Type"
        self.__age          = 10

#2B
    #Setters
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    #Getters
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age



# TEST:
pet = Pet()
pet.set_name("Cow")
pet.set_animal_type("Mammal")
pet.set_age(50)
print(pet.get_name())
print(pet.get_animal_type())
print(pet.get_age())

