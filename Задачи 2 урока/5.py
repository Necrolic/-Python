## Реализовать алгоритм перемешивания списка


import random

def chisla(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]
def mixing(lst):
    return random.shuffle(lst)
n = 20
lft = -100
rght = 100
spisok = chisla(n, lft, rght)
print(spisok)
mixing(spisok)
print(spisok)