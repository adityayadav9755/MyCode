a=int(input("Enter the number."))
b,c=0,0
d=a
while a>0:
    b=a%10
    a=a//10
    c=c+b**3
print(c)
if c==d:
    print("The number is Armstrong number.")
else:
    print("The number is not Armstrong number.")
# Examples of Armstrong Number:0, 1, 153, 370, 371 and 407