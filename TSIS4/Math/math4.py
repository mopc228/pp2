def parallelogram(a, h):
    return a*h
a = int(input("Введите длину параллелограма: "))
h = int(input("Введите высоту параллелограма: "))
print("Площадь параллелограма - " + str(parallelogram(a, h)))