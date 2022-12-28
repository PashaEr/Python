# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# number_list = input('Введите числа через пробел ').split()
# new_list =[]
# for el in number_list:
#     new_list.append(int(el))

# print(number_list)
# print(f'MAX = {max(new_list)} MIN = {min(new_list)}')

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#   1) с помощью математических формул нахождения корней квадратного уравнения
    
#   2) с помощью дополнительных библиотек Python

import math

a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if D == 0:
    x1 = (-b - math.sqrt(D)) / (2*a)
    print(x1)
elif D > 0:
    x1 = (-b - math.sqrt(D)) / (2*a)
    x2 = (-b + math.sqrt(D)) / (2*a)

    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)







    
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
