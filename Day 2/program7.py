# Python program to print all words that
#consist same set of characters.
from collections import Counter
def same_characters(input):
    dict={}
    for word in input:
        wordDict=Counter(word)
        key=wordDict.keys()
        key=sorted(key)
        key="".join(key)
        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key]=[]
            dict[key].append(word)
    print(dict)
same_characters(['may','student','students','dog','studentssess','god','cat','act','tab','bat','flow','wolf','lambs','amy','yam','balms','looped','poodle'])