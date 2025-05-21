#check if a number is perfect square or not
import math
def IsPerfectSquare(n):
    sq_root=int(math.sqrt(n)) #math.sqrt() returns square root of given number, including all the decimal values, so int() returns only the int part
    return sq_root*sq_root==n
number=int(input("enter number: "))
print(IsPerfectSquare(number))    