#problem1: check if a given is prime or not
# a number is prime if it is only divisible by 1 and it self
#below is the program which return True for prime numbers and False for composite numbers
def IsPrime(n):
    if n<=1:
        return False
    for i in range(2,n):      #checking if the numbr is divisible by any number other than 1 and itself
        if n%i==0:
            return False
    return True    
print(IsPrime(int(input('Enter number: '))))
  
#-----------------------------------------
#Other way (Typically for large numbers) using sympy module and isprime function
#---------------------------------------
from sympy import isprime
def Find_prime(n):
    return isprime(n)
print(Find_prime(int(input('Enter numbr: '))))