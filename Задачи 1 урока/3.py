## Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x, y = int(input("Введите координату x: ")), int(input("Введите координату y: "))
if x > 0 and y > 0:
    print("Точка в 1-ой четверти  плоскости")
elif x < 0 and y > 0:
    print("Точка во 2-ой четверти  плоскости")
elif x < 0 and y < 0:
    print("Точка в 3-ей четверти  плоскости")
elif x > 0 and y < 0:
    print("Точка в 4-ой четверти  плоскости")
