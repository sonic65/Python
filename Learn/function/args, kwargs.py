import pdb

def fun(*args,**kwargs):
    print("args: ", args)
    print("---------------")
    print("kwaras ", kwargs)

fun(1)

pdb.set_trace()

fun(1,2,3,a=1)
fun(a=1)


# *args表示任何多个无名参数，它是一个tuple
# **kwargs表示关键字参数，它是一个dict
