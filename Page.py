s=10
a=[]
po=2
cods=2
i=0
j=0
for i in range (0,po):
	col=[]
	for j in range (0,cods):
		b=int(input(""))
		col.append(b)
	a.append(col)
e=0
x=0
y=0
for x in range(0,s):
	for y in range(0,s):
		if x==a[y][0] and y==a[y][1]:
			print("*")
		else:
			print(" ")