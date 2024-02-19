n = int(input("Введите N: "))
a = (i for i in range(0, n))
mylist = []
for j in a:
    if j % 3 == 0 and j % 4 == 0:
        mylist.append(str(j))
x = ", ".join(mylist)
print(x)