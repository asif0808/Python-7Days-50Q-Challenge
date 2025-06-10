# Implement a stack using lists
class Stack:
    def __init__(self):
        self.lst=[]
        self.top=-1
    def add(self,val):
        self.lst.append(val)
        self.top+=1
    def remove(self):
        if self.top==-1:
            print("stack underflow")
            return
        self.lst.pop()
        self.top-=1
    def show(self):
        print(self.lst)
    def showtop(self):
        if self.top==-1:
            print("stack is empty")
        else:
            print(self.lst[self.top])
obj=Stack()
obj.show()
obj.add(2)
obj.add(3)
obj.add(9)
obj.show()
obj.showtop()
obj.remove()
obj.show()
obj.showtop()