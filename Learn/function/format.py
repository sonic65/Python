print("{1}{0}{0}".format("hello","python"))

print("姓名：{name}, 年龄：{age}, 性别：{sex}".format(name="Reimi", age="16", sex="girl"))

#通过字典查询
char={"name":"MuQ", "age": "14", "talent": "Knowledge"}
print("姓名：{name}, 年龄：{age}, 能力：{talent}".format(**char))

#通过列表索引查询
char_list=['Reimu', '18', 'taisan', 'MuQ', "14", "Knowledge"]
print("姓名：{0[0]}, 能力：{0[5]}".format(char_list))

#传入对象
class AssignValue(object):
    def __init__(self,value):
        self.value = value

my_value = AssignValue(2)
print("value: {0.value}".format(my_value))
