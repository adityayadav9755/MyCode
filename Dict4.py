nos = {'1':"One", '2':"Two",'3':"Three", '4':"Four", '5':"Five", '6':"Six", '7':"Seven", '8':"Eight", '9':"Nine", '10':"Ten"}
n = list(input("Enter the no:"))
name=""
for x in range(0,len(n)):
    name = name + nos[n[x]] + " "
print(name)
    
    