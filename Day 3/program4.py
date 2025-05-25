#program to Convert a list of tuples into a dictionary.
# def tuple_to_dict(data):
#     mydict=dict(data)
#     return mydict
# print(tuple_to_dict([(1,2),(2,4),(4,8)]))

#another way
def tuple_to_dict(data):
    mydict={}
    for key,val in data:
        mydict[key]=val
    return mydict
print(tuple_to_dict([(1,2),(1,4),(4,8)]))
