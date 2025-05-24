# Rotate a list k elements to the right.
#rotating a list to right means--------e.g. lst=[1,2,3,4,5] rotate 2 elements right means shift last 2 elements to front i.e. [4,5,1,2,3]
def reverse_list(lst,start,end):
    while start<end:
        lst[start],lst[end]=lst[end],lst[start]
        start+=1
        end-=1
def rotate_list(lst,k):
    n=len(lst)
    k=k%n      #for tackling k>n case
    #reversing whole list
    reverse_list(lst,0,n-1)
    #reversing list from starting to k-1
    reverse_list(lst,0,k-1)
    #reversing list from k to last
    reverse_list(lst,k,n-1)
lst=[1,2,3,4,5]
rotate_list(lst,3)
print(lst)