# Program to Sort a dictionary by values.
def sort_by_value(mydict):
    sorted_dict=dict(sorted(mydict.items(),key= lambda item:item[1]))
    return sorted_dict
print(sort_by_value({1:2,3:9,2:6}))