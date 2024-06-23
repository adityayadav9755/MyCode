n,a,b=5,1,0
num=[[0 for i in range(n)]for j in range(n)]

for x in range(n):
    num[b][x]=a
    a+=1
for y in range(1,n):
    num[y][n-b-1]=a
    a+=1
    
for x in range(2,n+1):
    num[n-b-1][-x]=a
    a+=1
for y in range(2,n):
    num[-y][b]=a
    a+=1
b+=1
    
for x in range(1,n-1):
    num[b][x]=a
    a+=1
for y in range(2,n-1):
    num[y][n-b-1]=a
    a+=1
b+=2
    
for x in range(3,n):
    num[b][-x]=a
    a+=1
for y in range(1,n-2):
    num[n-b][y]=a
    a+=1

for i in range(n):
    for j in range(n):
        if num[i][j]<10:
            print("0",end='')
        print(num[i][j],end=' ')
    print()