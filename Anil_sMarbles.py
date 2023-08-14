''' Anil has 'n' marbles.He is playing with his friend Raghu.They have made 4 holes in ground namely A, B, C and D.Anil throws all 'n' marbles one by one towards the holes.
If a marble lands in either hole A or C then Anil gets the marble back but if it lands in either B or D then Raghu receives the marble.
Now, you are given an array with 'n' numbers ranging from 1 to 10 depicting the speed of the marble.There are some conditions about speed based on which a marble lands in a hole.
The conditions are-:
A:- Speed < 6, Odd
B:- Speed < 6, Even
C:- Speed > 5, Even
D:- Speed > 5, Odd.
You have to write a program to print the number of marbles with Anil and Raghu after the end of the game.'''

a=[]
i=0
n=int(input("Enter the number of marbles."))
A=0
R=0
for i in range(0,n):
 b=int(input())
 a.append(b)
 if a[i]<6 and a[i]%2==0 or a[i]>5 and a[i]%2!=0:
   R+=1
print("Anil's Marbles=", n-R)
print("Raghu's Marbles=", R)
