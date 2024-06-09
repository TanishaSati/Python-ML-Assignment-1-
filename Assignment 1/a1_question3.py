#Factorial of a given number
a=int(input("Enter a given number : "))
fact=1
for i in range(1,a+1):
    fact*=i
print("The factorial of ",a,"is :",fact)