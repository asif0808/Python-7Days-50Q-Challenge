#implement own split method for string
def my_split(string):
    result=[]
    word=''
    for s in string:
        if s==" ":
            if word:     #what if there are more spaces at starting of a word
                result.append(word)
                word=''
        else:
            word+=s
    if word:      #what if there are spaces at the end
        result.append(word)
    return result
print(my_split("hello there  "))
print(my_split("    hello    there"))
