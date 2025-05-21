#implement calculator using functions and operator module
import operator
def calci(num1,num2):
    choice=int(input("enter your choice : 1.add 2.subtract 3.multiplication 4.Division ---->"))
    match choice:
        case 1:
            print('Sum is: {}'.format(operator.add(num1,num2)))
        case 2:
            print('Subtract is: {}'.format(operator.sub(num1,num2)))
        case 3:
            print('Multiplication is: {}'.format(operator.mul(num1,num2)))
        case 4:
            print('Division is: {}'.format(operator.truediv(num1,num2)))
        case _:
            print('wrong choice')
num1=int(input('enter first number: '))
num2=int(input('enter second number: '))
calci(num1,num2)