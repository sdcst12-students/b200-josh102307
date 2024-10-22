mylist = [5,10,15,2,4,6,8,-2,-4,-6,2,4,6,0.1]
sorted = []
for i in mylist:
    if i not in sorted:
        sorted.append(i)
        sorted.sort()
print(sorted)

