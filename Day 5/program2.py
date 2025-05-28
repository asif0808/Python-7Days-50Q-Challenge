# Find and replace text in a file.
with open('programs.txt','r') as file:
    content=file.read()
    #print(type(content))
updated_content=content.replace("In","RCB")
with open("programs.txt","w") as file:
    file.write(updated_content)
    
