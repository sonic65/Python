#调用

class SalaryAcc():
    def __call__(self,*args,**kwargs):
        print("sallry")
        return 3000

s = SalaryAcc()
s()        