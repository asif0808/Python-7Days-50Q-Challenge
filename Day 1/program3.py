#Converting string to title case without using title()
def Title_case(s):
    s=s.split()
    r=[]
    for ch in s:
        ch=ch.capitalize()
        r.append(ch)
    r=' '.join(r)
    return r
string=input("enter string : ")
print(Title_case(string))