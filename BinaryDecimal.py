def bd(a):
	b=0
	n=0
	out=0
	while a>0:
		# Finding the digit
		b=a%10
		#Check if digit is only 0 or 1
		if b==0 or b==1:
			#Formula for binary to decimal
			out+=b*(2**n)
			#Increasing value of n 
			n+=1
			# 1//10=0
			if a!=1:
				a=a//10
			else:
				break
		else: 
			print("This number is not binary.")
			break
	return out

def db(a):
	b=0
	n=0
	out=0
	while a>0:
		#Formula for decimal to binary
		b=a%2
		out+=b*(10**n)
		n+=1
		a=a//2
	return out



choice=int(input("Choose 1:Binary to Decimal  or   2:Decimal to Binary."))
a=int(input("Enter the number."))
#Checking the choice.
if choice==1:
	print(bd(a))
elif choice==2:
	print(db(a))
else:
	print("Choose correctly!")