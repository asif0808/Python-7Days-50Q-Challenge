# Remove nth node from end of list (using logic not Linked List).
def deleted_end(data,n):
    idx=len(data)-n 
    data.pop(idx)
    return data
print(deleted_end([2,3,4,5,6],2))