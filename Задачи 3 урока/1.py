## Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.


def sum_index(lst):
    a = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            a += nech[i]
    print(f"Сумма равна: {a}")
nech = list(map(int, input("Введите числа :\n").split()))
sum_index(nech)