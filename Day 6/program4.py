# Use property decorators for getter/setter.
class GetSet:
    def __init__(self,name):
        self._name=name
    @property
    # getter
    def name(self):
        return self._name
    # setter
    @name.setter
    def name(self,value):
        if not value:
            raise ValueError("Name should not be empty")
        self._name=value
obj=GetSet('aasif')
print(obj.name)
obj.name="john"
print(obj.name)
