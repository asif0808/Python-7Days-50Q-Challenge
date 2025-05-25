# Find the key with the maximum value in a dictionary
def find_max(data):
    maximum=float('-inf')
    for val in data.values():
        maximum=max(val,maximum)
    for key in data.keys():
        if data[key]==maximum:
            return key
print(find_max({1:3,2:5,3:1,9:33}))
 #Or
def find(data2):
    return max(data2,key=data2.get)
print(find({2:44,1:43,0:99}))
        