#check if two strings are anagrams
# An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once
def check_anagram(string1,string2):
    string1=string1.replace(" ","").lower()
    string2=string2.replace(" ","").lower()
    # print(sorted(string1))
    # print(sorted(string2))
    return sorted(string1)==sorted(string2)
string1=input('enter first string: ')
string2=input("enter second string: ")
print(check_anagram(string1,string2))