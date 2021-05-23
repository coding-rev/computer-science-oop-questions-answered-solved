#Question 3
# 3A & B - CLASS
class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name    = employee_name         
        self.__employee_number  = employee_number
    

    #Mutators
    def set_employee_name(self, name):
        self.__employee_name = name

    def set_employee_number(self, number):
        self.__employee_number = number
    
    #Accessor
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

# 3C & D - SUBCLASS
class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, payrate):
        self.__shift_number     = shift_number
        self.__hourly_payrate   = payrate
        # Initializing SuperClass through SubClass
        Employee.__init__(self, employee_name, employee_number)
        
    #Mutators
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_payrate(self, payrate):
        self.__hourly_payrate = payrate
    
    
    #Accessor
    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_payrate(self):
        return self.__hourly_payrate

       



# TEST:
# - Fetching SuperClass Methods through SubClass
user = ProductionWorker("Employee Name", "Employee number", 2, 500)
print(user.get_employee_name())
# - SubClass local Fetchs
print(user.get_shift_number())


