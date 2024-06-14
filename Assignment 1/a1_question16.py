#counting number of characters in a string 


str=input("Enter a string : ")
dict={}
for i in range(len(str)):
    if(str[i] in dict):
        dict[str[i]]+=1
    else:
        dict[str[i]]=1
for i in dict:
    print(i , ": ",dict[i])
        
