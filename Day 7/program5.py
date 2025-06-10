# Binary search in a sorted list
def bin_search(a,ele):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if ele<a[mid]:
            high=mid-1
        elif ele>a[mid]:
            low=mid+1
        else:
            return f"element found at index {mid}"
    return "not found"
print(bin_search([2,3,4,5,6],6))

#using recursion'
def recursion_binary(data,ele):
    def bin_search(low,high):
        if low>high:
            return "not found"
        mid=(low+high)//2
        if ele<data[mid]:
            return bin_search(low,mid-1)
        elif ele>data[mid]:
            return bin_search(mid+1,high)
        else:
            return mid
    return bin_search(0,len(data)-1)
print(recursion_binary([1,2,3,4,5],4))
        
