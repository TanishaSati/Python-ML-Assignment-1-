#Program readig data from csv file and print it to console
import csv
f=open("./mycsv.csv",'r')
stureader=csv.reader(f)
print("The content of My csv File : ")
for i in stureader:
    print(i)

