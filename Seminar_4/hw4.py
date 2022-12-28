
# 1. Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# Решение с числом ПИ

# from math import pi

# d = int(input("Введите число для заданной точности числа Пи: "))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


# Попобовал через Decimal, но так и не понял как он работает((

# import os
# os.system('cls')
# from decimal import Decimal
 

# x = int(input('Введите x:'))
# y = int(input('Введите y:'))

# print(x)
# print(y)
# x = Decimal(x)
# y = Decimal(y)

# print(x)
# print(y)
# x = x + y

# print(x)

# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# import math 

# num =int(input('Введите число: '))

# def prime_factors(num):  
#     while num % 2 == 0: 
#         print(2,) 
#         num = num / 2 
 
#     for i in range(3, int(math.sqrt(num)) + 1, 2): 

#         while num % i == 0: 
#             print(i,) 
#             num = num / i 
#     if num > 2: 
#         print(num) 



# prime_factors(num)

# 3. Задайте последовательность чисел. Напишите программу, которая уберёт одинаковые элементы 
# исходной последовательности.

import os
os.system('cls')

list = input(f'Ввведите значения списка через пробел: ').split()
print('\n')
print(list,'\n')
list_1 = []
for i in list:
    if i in list_1:
        continue
    else:
        list_1.append(i)
	        
print(list_1) 





