#simple exception functionality
class Division:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def div(self):
        try:
            Result=self.x/self.y
        except Exception as e:
            print("Error",e)
        else:
            print(Result)
        finally:
            print("this block executes always")
obj=Division(3,8)
obj.div()