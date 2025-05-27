# Check if a number is an Armstrong number
#a number is called armstrong if all digits power total numbers of digit sum equal to number itself
#ex: 153= 1^3+5^3+3^3=1+125+27=153
def IsArmstrong(number):
    number=str(number)
    power=len(number)
    res=0
    for n in number:
        res+=int(n)**power
    if res==int(number):
        return True
    else:
        return False
print(IsArmstrong(153))
    