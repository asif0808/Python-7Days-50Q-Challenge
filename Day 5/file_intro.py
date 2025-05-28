#creating a file
with open('ex.txt','w') as file:
    file.write("hello there")
#overwriting the data of file
with open('ex.txt','w') as file:
    file.write("hello , how are you?")
#reading data from a file
try:
    with open('ex.txt','r') as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("file not found")
#appending data into a file
with open('ex.txt','a') as file:
    file.write(" this is aasif \n")
with open('ex.txt','a') as file:
    file.write("Full stack python developer \n")
#reading data again
with open('ex.txt','r') as file:
    content=file.read()
    print(content)
#r+ mode (file must exist)
with open('ex.txt','r+') as file:
    file.write('this from r+')
    content=file.read()       #not updated becasye first read then write
    print(content)
#reading data again
with open('ex.txt','r') as file:
    content=file.read()
    print(content)
#w+ mode (write and read)  if file doesnt exist, new file will be created
with open('ex.txt','w+') as file:
    file.write('this is from w+')          #pointer/controller is at the end, so move it to starting otherwise it prints nothing
    file.seek(0)
    content=file.read()
    print(content)
