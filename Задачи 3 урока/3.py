## Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.


lists = list(map(float, input("Введите числа :\n").split()))
new_lists = [round(i%1,2) for i in lists if i%1 != 0]
print(max(new_lists) - min(new_lists))