a=int(input("Enter the number."))
b,c=0,0
while a>0:
    b=a%10
    a=a//10
    c=c*10+b
print(c)