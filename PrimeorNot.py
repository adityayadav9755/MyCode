x = int(input("Enter a number."))
c=0
if x<2:
	print(x, "is not prime.")
else:
	for n in range(2,x):
		if (x % n) == 0:
			c+=1
			break
	if c>0:
		print(x, "is not prime.")
	else:
		print(x, "is prime.")	
