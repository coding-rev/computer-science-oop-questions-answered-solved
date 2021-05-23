#Question 1
# 1A
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make       = make
        self.__speed      = 0

#1B
    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self):
        self.__speed = self.__speed - 5

    def get_speed(self):
        return self.__speed



# TEST:
car = Car(2020, "Toyota")
car.accelerate()
car.accelerate()
car.brake()
print(car.get_speed())

