n=eval(input("Enter the numbers in list form."))
a=n[1]
for i in n:
    if i<a:
        a=i
print(a)