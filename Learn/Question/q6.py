# 利润
# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成

def earn():
    i = int(input('请输入利润: '))
    e = 0

    if i <= 10:
        e = i*0.1
        print(e)
    elif (i>10) and (i<30):
        e = (30-i)*0.2 + 10*0.1
        print(e)
    elif (i>60) and (i<100):
        e = (i-60)*0.15 + 10*0.1
        print(e)


earn()
# if i > 10 and i < 20:
#     e = (20-i)*0.1

# #提成
# # print(e)

