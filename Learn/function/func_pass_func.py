def hi():
    return "hi sonic"

def doSomethingBeforeHi(func):
    print("Before hi()")
    print(func())

doSomethingBeforeHi(hi)