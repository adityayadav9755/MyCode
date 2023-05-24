a=int(input("Enter first number."))
b=int(input("Enter second number."))
e=5
g=int(input("Select the mode. ADD=1. SUBTRACT=2. MULTIPLY=3. DIVIDE=4")) 
while e>0{
	if g==1:
		c=a+b
		d=int(input("Enter the answer."))
		if c==d:
			print("Correct")
		else:
			print("Incorrect")
	elif g==2:
		c=a-b
		d=int(input("Enter the answer."))
		if c==d:
			print("Correct")
		else:
			print("Incorrect")
	elif g==3:
		c=a*b
		d=int(input("Enter the answer."))
		if c==d:
			print("Correct")
		else:
			print("Incorrect")
	else:
		c=a/b
		d=int(input("Enter the answer."))
		if c==d:
			print("Correct")
		else:
			print("Incorrect")
	e-=1
}
	