w=eval(input("Enter the words in list form."))
l=[]
n=int(input("Words should be longer than __?"))
for i in w:
    a=str(i)
    if len(a)>n:
        l.append(a)
print(l)
    