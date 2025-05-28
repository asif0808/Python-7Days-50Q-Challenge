with open('ex2.txt','w+') as file:
    file.write("hello this is second \n")
    file.write("second this is \n")
    file.write("this in second\n")
    file.write("example number second\n")
    file.seek(0)
    content=file.read()
    print(content)
    #reading line by line
    file.seek(0)
    line_by_line=file.readlines()
    #print(line_by_line)   returns list collection of each line 
    #calculating number of lines in text file
    count=0
    for line in line_by_line:
        count+=1
        print(line.strip())
    print("total line in file: ",count)