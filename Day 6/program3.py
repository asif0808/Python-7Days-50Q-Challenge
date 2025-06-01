# Use @staticmethod and @classmethod appropriately.
class Example:
    #constructor
    def __init__(self):
        print("class created")
    #instance method
    def instance(self):
        print("this is instance method")
    @classmethod
    def class_method(cls):
        print("this is a class level method")
    @staticmethod
    def static_method():
        print("this is a static method")
obj=Example()
obj.instance()
Example.class_method()
Example.static_method()