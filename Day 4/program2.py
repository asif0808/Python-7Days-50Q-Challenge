# Compute nth Fibonacci number using memoization.
#below code is without memorization which is not good for large numbers
def fibonacci(n):
    if n==1 or n==0:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))

#with memorization
from functools import lru_cache
@lru_cache
def fibonacci_memorization(num):
    if num<=1:
        return num
    return fibonacci_memorization(num-1)+fibonacci_memorization(num-2)
print(fibonacci_memorization(40))
    