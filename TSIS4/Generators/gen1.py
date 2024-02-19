n = int(input("Введите число N: "))
a = (i**2 for i in range(0, n))
for j in a:
    print(j)