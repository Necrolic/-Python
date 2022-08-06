## Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.


def fibo(k: int) -> list:
    fibo_list = [-1, 1, 0, 1, 1]
    for i in range(3, k+1):
        fibo_list.append(fibo_list[-2] + fibo_list[-1])
        fibo_list.insert(0, fibo_list[1] - fibo_list[0])
    return fibo_list
k = 0
while k < 2:
    k = int(input('число большее 2: '))
if k < 2:
        print('Ошибка ')   
fibo_list = fibo(k)
print(fibo_list)