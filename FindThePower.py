a=int(input("Enter the base:"))
b=int(input("Enter the number:"))
i=0
n=1
while n<b :
    n=n*a
    i+=1
if n==b:
    print(i)
else:
    print("No such integral power exists.")

