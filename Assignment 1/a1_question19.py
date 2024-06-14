#To remove all puctuation from a string
str=input("Enter a string ")
newStr=""
for i in str:
    if(i.isalpha()):
        newStr+=i
    elif i.isspace():
        newStr+=i


print("Updated string is ",newStr)
