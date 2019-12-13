

data=open("data.txt","r",encoding="utf-8")
values=data.readlines()
data.close()

for value in values:
    #文件中每一个关键字之间使用“，”隔开，因此在代码中也使用“,”来区分不同的关键字
    cn_name=value.split(",")[0]
    print(cn_name)
    en_name=value.split(",")[1]
    print(en_name)
    other=value.split(",")[2]
    print(other)