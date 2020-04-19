class MusicPlayer(object):

    def __init__(self):
        print("Play Music")


    def __new__(cls,*args,**kwargs):
        print("initializing")    

        instance = super().__new__(cls)
        return instance



player = MusicPlayer()

print(player)
