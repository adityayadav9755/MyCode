#Special string is defined as the string with 2 or more characters and its first and last charcters are same.

n=eval(input("Enter the strings in list form."))
count=0
for i in n:
    a=str(i)
    if a[0].lower()==a[len(a)-1].lower():
        if len(a)>1:
            count+=1
print(count)