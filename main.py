
'''
На входе функция получает параметр n - натуральное число. Необходимо сгенерировать n-массивов,
заполнить их случайными числами, каждый массив имеет случайный размер. Размеры массивов не должны совпадать.
Далее необходимо отсортировать массивы. Массивы с четным порядковым номером отсортировать по возрастанию,
с нечетным порядковым номером - по убыванию. На выходе функция должна вернуть массив с отсортированными массивами.
'''
import random

def arrgen(n):
    arr=[]
    for i in range(0, n):
        arr.append(random.randint(1, 5))
    return arr

def sizesgen(n):
    sizes = []
    while len(sizes) != n:
        s = random.randint(2, 10)
        if s not in sizes:
            sizes.append(s)
    return sizes

def sorting(result):
    for i in range(len(result)):
        if (i + 1) % 2 == 0:
            result[i].sort()
        else:
            result[i].sort(reverse=True)
    return result

result = []
sizes = sizesgen(int(input("Введите параметр n: ")))
for i in sizes:
    result.append(arrgen(i))

print(sorting(result))


