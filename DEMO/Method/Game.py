class Game(object):

    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("Help 1.xxx")

    @classmethod
    def show_top_score(cls):
        print("High Score %d" % cls.top_score)

    def start_game(self):
        print("%s Start The Game" % self.player_name)      

#1.show help (staticmethod,直接使用类名调用静态方法)
Game.show_help()

#2.show high_score (classmethod,直接使用类名调用类方法)
Game.show_top_score()

#3.start_new_game (instance,创造一个实例,调用方法)
game = Game("sonic")
game.start_game()



#Requirement
# top_score #Hight Score (Class_method)
# player_name #Name (Instance)
# show_help #Maual (Static_Method)
# start_game #New Game (Instance)
# ##