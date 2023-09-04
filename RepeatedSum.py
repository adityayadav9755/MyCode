n=int(input("Enter the limit"))
a=0
for i in range(1,n+1):
    a=a+i*(n-i+1)
print(a)
k=1
c=0
while k<=n:
    j=1
    k+=1
    b=0
    while j<=k:
        b=b+j
        j+=1
    c=c+b
print(c)