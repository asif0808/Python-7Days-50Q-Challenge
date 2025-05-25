# Create a dictionary from two lists
def create_dict_list(list1,list2):
    if len(list1)!=len(list2):
        return False
    mydict={}
    for key,val in zip(list1,list2):
        mydict[key]=val
    return mydict
print(create_dict_list([1,2,3],[2,4,6]))