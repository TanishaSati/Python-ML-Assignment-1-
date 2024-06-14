#WAP to convert temperature into other unit , celsius to fahreneheit
temp=float(input("Enter the temperature : "))
unit=input("Enter the unit of above temperature : ")
if(unit=='F'):
    cel_temp=(temp-32)*5.0/9
    print("fahreneheit : ",temp,"F and in celsius : ",cel_temp,"C")
elif(unit=='C'):
    fah_temp=(temp*9/5)+32
    print("celsius : ",temp,"C and in fahreneheit : ",fah_temp,"F")
else:
    print("Enter a valid unit 'F' or 'C")
