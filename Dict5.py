friends = {}
n= int(input("Enter the no. of friends :"))
for x in range (1,n+1):
    name = input(f"Enter the name of friend {x} :")
    no = int(input(f"Enter the salary of friend {x} :"))
    friends[name] = no
    
def A(dic):
    return dic

def B(dic):
    dic['Aditya'] = 9755410901
    return dic

def C(dic):
    del dic['Aditya']
    return dic

def D(dic):
    dic['A'] = 4
    return dic

def E(dic):
    return A in dic

#def F(dic):
#   return dic.sorted()

print(A(friends))
