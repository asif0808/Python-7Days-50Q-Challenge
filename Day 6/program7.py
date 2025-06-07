class NameValidation(Exception):
    pass
def check(input):
    if not input.isalpha():
        raise NameValidation("just alphabets allowed")
try:
    input=input("enter name: ")
    check(input)
except NameValidation as e:
    print(e)
else:
    print("Name is :",input)
    