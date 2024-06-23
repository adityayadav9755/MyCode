# This program checks if a relation is equivalence relation or not

a = eval(input("Enter the set on which relation is defined:\n"))
r = eval(input("Enter the relation:\n"))


def ref(x):
    """
    :param x: relation to be checked
    :return: true if relation is reflexive
    """
    for i in a:
        if (i, i) not in x:
            return False
    return True
    

def sym(x):
    """
    :param x: relation to be checked
    :return: true if relation is symmetric
    """
    for elem in x:
        if (elem[1], elem[0]) not in x:
            return False
    return True


def tran(x):
    """
    :param x: relation to be checked
    :return: true if relation is transitive
    """
    for i in x:
        for j in x:
            if i[1] == j[0]:
                if (i[0], j[1]) not in x:
                    return False
    return True


if ref(r) and sym(r) and tran(r):
    print("The given relation is an equivalence relation.")
else:
    print("The given relation is not an equivalence relation.")
