class AgeError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.error= errorInfo
    
    def __str__(self):
        return "***age error***"

if __name__ == "__main__":
    age = int(input("input an age : "))
    if age <1 or age>150:
        raise AgeError(age)
    else:
        print("right",age)