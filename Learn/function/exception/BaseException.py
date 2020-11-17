import traceback

try:
    print("setp1")
    a = 3/0
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
    print(type(e))
    #open()参数a附件 w覆盖
    with open("E:\Work\Project\Python\Learn\exception\e.txt","a") as f:
        traceback.print_exc(file=f)

print("step4")