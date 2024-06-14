 #read multiple lines of input from user until they enI am tanishater an empty line & print all the lines 
lines=[]
while True:
    line=input("Enter a line : ")
    if(line==""):
        break
    lines.append(line)
print("The content you have added till now ")
for line in lines:
    print(line)