def digits(n): 
	digit=0
	while (n>0):
		n=n//10
		digit+=1
	print(digit)
digits(int(input("")))
