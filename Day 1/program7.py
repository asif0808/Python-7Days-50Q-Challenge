#reverse digit of an integer without converting it to string
#logic is let say there is a number 123 if we divide it by 10 then remainder will be 3 and in next step for 12 remainder will be 2 and further it will be 2
# so after multiplying by 10 we will get reverse --> 321
def reverse(num):
    neg=num<0
    num=abs(num)
    ans=0
    while num:
        ans=(ans*10)+(num%10)
        num=num//10
    return -ans if neg else ans
num=int(input("enter number: "))
print(reverse(num))