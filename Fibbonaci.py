x=int(input("Enter the maximum no."))
a,b,c=0,1,0
while a<=x:
	print(a)
	c=a+b
	a,b=b,c
