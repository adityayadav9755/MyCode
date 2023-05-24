n=int(input("Enter a number."))
if n%2==0:
 n+=1
i=0
print("* "*n)
for i in range(0,n-2):
 print("  "*(n//2 -1), " *")  
print("* "*n)