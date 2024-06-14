#Checks if two strings are anagram of each other
str1=input("Enter a string : ")
str2=input("Enter another string : ")
str1_list=list(str1)
for i in str2:
    if(i in str1_list):
        str1_list.remove(i)
if(str1_list==[]):
    print("The given string  is Anagram ")
else:
    print("The given string  is not  anagram ")
