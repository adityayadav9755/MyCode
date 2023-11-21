def func(m, n):
    for i in n:
        for j in m:
            if i != j:
                continue
            else:
                return True
                break
    return False


a = eval(input("Enter the list1 in list form."))
b = eval(input("Enter the list2 in list form."))
print("Do they have common element?", func(a, b))
