#Counting vowels and consonents in a given string
def Count_vowels_consonents(string):
    vowels="aeiouAEIOU"
    consonent_count=vowel_count=0
    for char in string:
        if char in vowels:
            vowel_count+=1
        else:
            consonent_count+=1
    return vowel_count,consonent_count
string=input("enter string: ")
vowels,consonents=Count_vowels_consonents(string)
print("vowels are : {} and consonents are: {}".format(vowels,consonents))