# Program to Invert a dictionary (keys to values and values to keys)
def Invert_dict(mydict):
    newdict={}
    for key,val in mydict.items():
        if val not in newdict.keys():
            newdict[val]=[key]
        else:
            newdict[val].append(key)
    return newdict
print(Invert_dict({1:2,2:4,3:6,5:6}))
