# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random as rand
# import os
# os.system('cls')



# l = int(input('Введите длину списка: '))
# ls = [rand.randint(1,50) for i in range(l)] # Заполнение списка рандомно числами от 1 до 50 

# new_ls = ls[1:l:2]
# sum_nefw_ls = sum(new_ls)
# print(ls)
# print(new_ls)
# print(f'Сумма чисел на нечетных позициях равна: {sum_nefw_ls }')


# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
import os
os.system('cls')



number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)

