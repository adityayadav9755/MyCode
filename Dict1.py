ODD = {1:"one", 2:"two",3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}
def I(dic):
    return dic.keys()

def II(dic):
    return dic.values()

def III(dic):
    return dic.items()
    
def IV(dic):
    return len(dic)
    
def V(dic):
    return 7 in dic
    
def VI(dic):
    return 2 in dic
    
def VII(dic):
    return dic[9]
    
def VIII(dic):
    del dic[9]
    return dic

print(VIII(ODD))
