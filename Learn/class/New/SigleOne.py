class MusicPlayer(object):
    #记录第一个被创建对象的引用
    instance = None

    #记录是否执行过初始化
    init_flag = False

    def __new__(cls,*args,**kwargs):
      #1 判断类属性是否为空对象
      if cls.instance is None:
      #2 调用父类的方法为第一个对象分配空间
          cls.instance = super().__new__(cls)
      #3 返回类属性保存的对象引用
      return cls.instance


    def __init__(self):

        if MusicPlayer.init_flag:
            return
        print("initialed") 

        MusicPlayer.init_flag = True    


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

#两个player内存地址不一样,表示2个实例

#单例:系统中只有唯一的一个实例

