n=int(input("Enter the limit:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(" "*(n-i),end='')
        print("*",end='')
        if i>1:
            print(" "*(2*i-3),end='')
            print("*")
        else:
            print()