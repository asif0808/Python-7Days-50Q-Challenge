# Implement inheritance and method overriding.
# Inheritance is an object-oriented programming (OOP) feature that allows a class (child) to inherit attributes and methods from another class (parent)
class Outer:
    #constructo overriding
    def __init__(self):
        print("parent constructor")
    def show(self):
        print("this is from parent class")
class Inner(Outer):
    #constructor overriding
    def __init__(self):
        super().__init__()
        print("child constructor")
    def show(self):
        super().show()
        print("this is from child class")
    def myshow(self):
        print("this is from child class")
obj=Inner()
obj.myshow()
obj.show()
