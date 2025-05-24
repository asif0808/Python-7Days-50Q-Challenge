#write program to flatten a nested list
#let say the nested list dimension is 2
# def nested_to_flattend(nlist):
#     result=[]
#     for first in nlist:
#         for second in first:
#             result.append(second)
#     return result
# print(nested_to_flattend([[2,3,4],[4],[7,8,9]]))

#program for flatten list of unknown dimension (using recursion)
def nested_to_flattend(nlist):
    result=[]
    for item in nlist:
        if isinstance(item,list):
            result.extend(nested_to_flattend(item))
        else:
            result.append(item)
    return result
print(nested_to_flattend([2,3,[[4,5,6]],5,6]))
