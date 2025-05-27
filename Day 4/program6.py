# Find GCD and LCM of two numbers using functions.

#using python built-in function
from math import gcd,lcm
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
g=gcd(num1,num2)
l=lcm(num1,num2)
print(f"GCD of {num1} and {num2} is {g}")
print(f"lcm of {num1} and {num2} is {l}")

#without using builtin functions
def find_gcd(number1,number2):
    while number2:
        number1,number2=number2,number1%number2
    return number1
def find_lcm(number1,number2):
    return (number1*number2)//find_gcd(number1,number2)
number1=200
number2=250
print(find_gcd(number1,number2))
print(find_lcm(number1,number2))
