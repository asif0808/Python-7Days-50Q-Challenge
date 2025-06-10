# Sort a list using bubble sort and quicksort
# in bubble sort adjacent elements are swapped if they are in wrong order in each pass
def bubble_sort(data):
    n=len(data)
    for i in range(n):
        for j in range(n-i-1):
            if data[j]>data[j+1]:
                data[j+1],data[j]=data[j],data[j+1]
    return data
print(bubble_sort([2,1,5,3,3]))

def quick_sort(data2):
    if len(data2)<=1:
        return data2
    pivot=data2[0]
    left=[x for x in data2[1:] if x<=pivot]
    right=[x for x in data2[1:] if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
print(quick_sort([2,1,5,3,3]))