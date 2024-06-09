#first n numbers of fibonacci series
n=int(input("Enter a number "))
a=0
b=1
i=0
print(a ,end=" ")
print(b , end=" ")

while i<n:
    print(a+b,end=" ")
    temp=a
   
    a=b
    b=temp+a
    
    i+=1
    