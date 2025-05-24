#removing duplicates from a list
def remove_duplicates(values):
    result=[]
    for val in values:
        if val not in result:
            result.append(val)
    return result
print(remove_duplicates([2,3,4,5,2,3,9,70]))

#for in-place
def remove_inplace(values):
    i=0
    while i<len(values):
        if values.index(values[i])!=i:
            values.pop(i)
        else:
            i+=1
values=[2,3,4,5,2,3,9,70]
remove_inplace(values)
print(values)