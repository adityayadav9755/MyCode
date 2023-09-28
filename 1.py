a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
c=int(input("Enter 3rd no:"))
y=0
for x in [a,b,c]:
    if x>y:
        y=x
print(y)