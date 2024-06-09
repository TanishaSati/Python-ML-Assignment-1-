#writing string data to txt file
f=open("mynewfile.txt",'w')
data=input("Enter the data to be put into file : ")
f.write(data)
print("Content added to the file successfully")

