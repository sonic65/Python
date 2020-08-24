
def hello_world():
    print("Hello World")

def hello_multi():
    for i in range(3):
        hello_world()

if __name__ == '__main__':
    hello_multi()