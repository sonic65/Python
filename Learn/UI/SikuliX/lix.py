# coding=utf-8
from jpype import *
import jpype

jvmPath = getDefaultJVMPath()
print(jvmPath)
jpype.startJVM(jvmPath,'-ea',r'-Djava.class.path=/Users/gaoyuhang/Project/Python/Learn/UI/SikuliX/sikulixapi-2.0.4.jar')

jpype.java.lang.System.out.println("hello world")
java.lang.System.out.println("hello world")

javaclass = jpype.JClass('org.sikuli.script.Screen')    #引入SikuliX中的Screen类

s = javaclass()      #实例化Screen类得到对象
# s.doubleClick(r"/Users/gaoyuhang/Project/Python/Learn/UI/SikuliX/imge/Chrome.png")
s.capture(100,200,300,400)

jpype.shutdownJVM()          #关闭JVM

# # if  jpype.isJVMStarted() == True :
# app =JClass('org.sikuli.script.App')
# Screen = JClass('org.sikuli.script.Screen')
# Key = JClass('org.sikuli.script.Key')
# # Pattern = JClass('import org.sikuli.script.Pattern')
# # FindFail = JClass('org.sikuli.script.FindFailed')
# screen=Screen()
# key = Key()
# # screen.selectRegion()
# # screen.capture(100,200,300,400)
# screen.doubleClick("/imge/20181211194953.png")
# screen.type("/imge/20181128114943.png","http://192.168.16.107:8085/login")
# if screen.exists("/imge/20181128115419.png"):
#     screen.type(key.ENTER)
# screen.wait("/imge/20181128114200.png")
# screen.type("/imge/20181128114220.png","ddy")
# screen.type("/imge/20181128114232.png","1234567")
# screen.click("/imge/20181128114245.png")