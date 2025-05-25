#print the pattern 
#input a 4
#output          a aaaa
#                aa aaa
#                aaa aa
#                aaaa a
def pattern(input,num):
    for i in range(1,num+1):
        print(input*i, input*num)
        num=num-1
pattern('a',4)