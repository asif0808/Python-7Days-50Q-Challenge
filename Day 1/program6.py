#Largest of three numbers using only conditional expression
#a conditional expression is basically a ternary operator in python 
# execute_if if condition else execute_else
def LargestOfThree(a,b,c):
    largest=a if a>b and a >c else b if b>a and b>c else c
    return largest
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
print(LargestOfThree(a,b,c))