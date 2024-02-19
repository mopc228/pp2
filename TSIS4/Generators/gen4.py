a = int(input("Введите a: "))
b = int(input("Введите b: "))
squares = (i**2 for i in range(a, b))
for j in squares:
    print(str(j), end = " ")