# Implement linear search with early exit.
def linear_search(list,ele):
    for l in range(len(list)):
        if list[l]==ele:
            return f"found at index {l}" 
    return "not found"
print(linear_search([2,6,1,5,3],1))