emp = {}
n= int(input("Enter the no. of employees :"))
for x in range (1,n+1):
    name = input(f"Enter the name of employee {x} :")
    sal = int(input(f"Enter the salary of employee {x} :"))
    emp[name] = sal
print(emp)
