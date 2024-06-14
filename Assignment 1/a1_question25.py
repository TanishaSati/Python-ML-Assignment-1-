f=open("./myfile.txt",'r')
fnew=open("copiedFile.txt",'w')
data=f.readlines()
for line in data:
    fnew.write(line)
#Printing the content of copied file
fnew=open("copiedFile.txt",'r')
datanew=fnew.readlines()
for line in datanew:
    print(line)
    