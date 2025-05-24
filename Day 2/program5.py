#find longest word in a sentence
# def find(s):
#     res=''
#     s=s.split()
#     for i in range(len(s)-1):
#         if (len(s[i])>len(s[i+1])):
#             res=s[i]
#         else:
#             res=s[i+1]
#     return res
# print(find("I am learning Python programming language"))
 
#optmised way
def find(string):
    res=""
    for s in string.split():
        if len(s)>len(res):
            res=s
    return res
print(find("I am learning programming language"))


