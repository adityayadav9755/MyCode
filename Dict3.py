cnt = {}
a = list(input("Enter the string:"))
for x in a:
    if x not in cnt:
        cnt[x] = a.count(x)
print(cnt)