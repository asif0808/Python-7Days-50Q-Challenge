#. Merge contents of two files line by line.
#this will merge till the shorter length file
with open("ex2.txt","r") as file1,open("programs.txt","r") as file2,open("merged.txt","w") as merged:
    for line1,line2 in zip(file1,file2):
        merged.write(line1.strip()+' '+line2)
#merging total lines
from itertools import zip_longest
with open("ex2.txt","r") as file1,open("programs.txt","r") as file2,open("total_merged.txt","w") as t_merged:
    for line1,line2 in zip_longest(file1,file2,fillvalue=' '):
        t_merged.write(line1.strip()+' '+line2)

