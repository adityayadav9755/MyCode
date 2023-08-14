def bd(a):
	b,n,out=0,0,0
	while a>0:		
		b=a%10                       # Finding the digit		
		if b==0 or b==1:             #Check if digit is only 0 or 1			
			out+=b*(2**n)        #Formula for binary to decimal			 
			n+=1                 #Increasing value of n			
			if a!=1:             # 1//10=0
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
		b=a%2                        #Formula for decimal to binary
		out+=b*(10**n)
		n+=1
		a=a//2
	return out

choice=int(input("Choose 1:Binary to Decimal  or   2:Decimal to Binary."))
a=int(input("Enter the number."))
if choice==1:                                #Checking the choice.
	print(bd(a))
elif choice==2:
	print(db(a))
else:
	print("Choose correctly!")
