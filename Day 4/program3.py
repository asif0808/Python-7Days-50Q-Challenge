# Print all permutations of a string.
from itertools import permutations
def permutations_string(string):
    all=permutations(string)
    #print(type(all))
    for i in all:
        print(i)
        print(''.join(i))
        #print(type(i))     ---------> <class 'tuple'>
permutations_string('hello')

#printing total numbers of possible permutations
def total_permutations(string1):
    count=0
    if len(string1)==0:
        return 0
    for i in permutations(string1):
        count+=1
    return count
print(total_permutations('Hello'))
