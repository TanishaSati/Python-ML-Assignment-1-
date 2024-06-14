#Simple calculator
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
operator=input("Enter operator + ,-,/,* ")
if(operator=='+'):
    print("sum :",a+b)
elif(operator=='-'):
    print("diff :",a-b)
elif(operator=='*'):
    print("product :",a*b)
elif(operator=='/'):
    print("sum :",a/b)
else:
    print("Enter a valid operator +,-,*,/")