n = int(input("N: "))
a = (i for i in range(n, -1, -1))
for j in a:
    print(str(j), end = " ")