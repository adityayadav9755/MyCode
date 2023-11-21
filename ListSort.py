n=eval(input("Enter the list in list form:"))
i,j=0,0
while i<len(n):
    k=i
    j=i+1
    a=n[i]
    while j>i and j<len(n):
        if n[j]<a:
            a=n[j]
            k=j
        j+=1
    n[k]=n[i]
    n[i]=a
    i+=1
print(n)      