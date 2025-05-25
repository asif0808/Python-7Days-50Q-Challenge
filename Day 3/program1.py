# Count frequency of elements in a list using dictionary.
# from collections import Counter
# def frequency(data):
#     result=Counter(data)
#     return result
# data=[1,2,1,2,1,3]
# print(frequency(data))

#another way using dictionary
def frequency(data):
    dict={}
    for val in data:
        if val not in dict.keys():
            dict[val]=1
        else:
            dict[val]+=1
    return dict
data=[1,2,1,2,1,1,0,3]
print(frequency(data))