n=int(input("Enter the limit:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>1:
            print(" "*(2*(n-i)),end='')
            print("*",end='')
        else:
            print(" "*(n-i),end='')
            print("*",end='')
        if i>1:
            print(" "*(2*i-3),end='')
            print("*",end='')
    print()
