

# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# # - 6782 -> 23
# # - 0,56 -> 11

# import os
# os.system('cls')

# n = input("Введите вещественное число: ")

# count = 0
# for i in n:
#     if i.isdigit():
#         count += int(i)
        
# print("Сумма цифр равна:", count)


# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# import os
# os.system('cls')


# N = int(input('Введите число N: '))
# sum = 1
# for item in range(2, N + 1):
#     print(sum, end=', ')
#     sum *= item
# print(sum)


# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число N: '))
my_list = []
sum_elements = 0


for item in range(1, n + 1):
    elem = round((item + (1 / item)) ** item,2)
    my_list.append(elem)
    sum_elements += elem
print(my_list)
print(sum_elements)









