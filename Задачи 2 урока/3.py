## Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму.


n = int(input('Введите число: ')) 
def var(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]
nums = var(n)
print(nums)
print(round(sum(nums), 5))