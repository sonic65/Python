from functools import wraps

def new_decorator(a_func):
    # @wraps(a_func)
    def wrapTheFunction():
        print("Beafor a_func()")
        a_func()
        print("After a_func()")
    return wrapTheFunction

@new_decorator
def requiring_decorator():
    """Decorator me"""
    print("Needs some decoration")

# requiring_decorator()
print(requiring_decorator.__name__)

# if @wraps(a_func) requiring_decorator.__name__ 为 wraps(a_func)
# else              requiring_decorator.__name__ 为 requiring_decorator