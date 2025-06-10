# Check if parentheses are balanced using a stack.
def check(string):
    stack=[]
    slist=list(string)
    for s in slist:
        if s=="(" or s=="{" or s=="[":
            stack.append(s)
        elif s==")" and stack[-1]=="(" or s=="}" and stack[-1]=="{" or s=="]" and stack[-1]=="[":
            if not stack:
                return False
            stack.pop()
        else:
            return False
    return len(stack)==0
print(check("[[}}]]"))