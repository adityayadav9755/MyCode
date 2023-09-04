a=int(input("Enter the base."))
b=int(input("Enter the power."))
c=1
while b>0:
    c=c*a
    b=b-1
print("Answer is:", c)