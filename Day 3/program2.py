# program to Merge two dictionaries. If same key, sum the values.
#WARNING::Avoid Using dict as keyword
def merge_dict(dict1,dict2):
    dict={}
    for key,val in dict1.items():
        dict[key]=val
    for key,val in dict2.items():
        if key not in dict.keys():
            dict[key]=val
        else:
            dict[key]+=val
    return dict
print(merge_dict({1:3,2:4},{5:2,2:4}))
