def hi(name="sonic"):
    print("this is inside the hi() function")

    def greet():
        return "this is in greet() function"
    
    def welcome():
        return "this is in welcome() function"
    
    print(greet())
    print(welcome())
    print("now you are backin the hi() function")


hi()