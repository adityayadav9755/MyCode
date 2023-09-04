n=int(input("Enter the number:"))
a=int(input("To be replaced:"))
b=int(input("To be replaced by:"))
c=0
i=0
while n>0:
    i+=1
    d=n%10
    n=n//10
    if d==a:
        d=b
    c=c+d*(10**(i-1))
print(c)