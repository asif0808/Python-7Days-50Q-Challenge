# Overload operators for a custom class.
class Calc:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #overload + operator
    def __add__(self,other):
        return Calc(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Calc(self.x-other.x,self.y-other.y)
    def __str__(self):
        return f"Result is : ({self.x},{self.y})"
    
obj=Calc(1,2)
obj2=Calc(2,3)
obj3=obj+obj2
print(obj3)
obj4=obj-obj2
print(obj4)