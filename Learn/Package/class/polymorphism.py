class Animal:
    def eat(self):
        print("eat food")


class Cat(Animal):
    def eat(self):
        print("cat eat fish")


class Dog(Animal):
    def eat(self):
        prin("dog eat bone")


class Bird(Animal):
    def eat(self):
        print("Bird eat bugs")


def AnimalEat(a):
    if isinstance(a,Animal):
        a.eat()
    else:
        print("undefine")

AnimalEat(Cat())