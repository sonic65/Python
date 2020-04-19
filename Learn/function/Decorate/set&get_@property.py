class Employee:

    def __init__(self,name,salary):
        self.__name = name 
        self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def set_salary(self,salary):
        if 1000<salary<3000:
            self.__salary = salary
        else:
            print("out of range")

emp1 = Employee("sonic",2000)
print(emp1.salary)
emp1.set_salary = 3000  #out of range
# emp1.set_salary = 2100
print(emp1.salary)
