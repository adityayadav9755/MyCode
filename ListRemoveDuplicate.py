n=eval(input("Enter the input in list form."))
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
            if count>1:
                n.remove(j)
print(n)