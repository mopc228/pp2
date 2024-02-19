import math
def polygon(n, l):
    s = (n*(l**2)*(math.tan(math.pi/n)**(-1)))/n
    return s
n = int(input("Введите количество сторон: "))
l = int(input("Введите длину стороны: "))
print("Площадь многоугольника - " + str(polygon(n, l)))