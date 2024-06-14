str=input("Enter a sentence : ")
start=input("Enter starting word ")
#Starting Word checking 
if(str.startswith(start)):
    print("Yes, it starts with ",start)

else:
    print("No, it do not  starts with ",start)

#ending Word checking 
end=input("Enter ending word : ")
if(str.endswith(start)):
    print("Yes, it end with ",end)

else:
    print("No, it do not end with ",end)
