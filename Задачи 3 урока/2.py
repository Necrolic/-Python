##Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def multi(pair):
    a = len(pair)//2 + 1 if len(pair) % 2 != 0 else len(pair)//2
    new_pair = [pair[i]*pair[len(pair)-i-1] for i in range(a)]
    print(new_pair)

pair = list(map(int, input("Введите числа :\n").split()))
multi(pair)