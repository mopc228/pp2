def trapezoidal(a,b,h):
    s = (a+b)*h/2
    return s
h = int(input("Введите высоту: "))
a = int(input("Введите первое основание трапеции: "))
b = int(input("Введите второе основание трапеции: "))
print(trapezoidal(a,b,h))