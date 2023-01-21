
# 1. функция lambda

# #  Напишите программу, удаляющую из текста все слова, содержащие "абв".

# text = 'пра праАБВ оарп аоаоповАБВ азвлаоылаы АБВитиВБ АБВ'

# text = text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
# print()
# print(' '.join(text))
# print()

# # 2.  функция filter


# numbers = [ 1,3,4, 6,8, 3, 5, 67, 734 ] # список чисел


# def filter_odd_num(in_num): # функция проверки чисел
#     if(in_num % 2) == 0:
#         return True
#     else:
#         return False



# out_filter = filter(filter_odd_num, numbers) # Применение filter() для удаления нечетных чисел

# print(numbers)
# print()
# print("Отфильтрованный список: ", list(out_filter))
# print()

# 3. функция map

# collection = range(3)
# my_list = list(collection)
# my_tuple = tuple(collection)
# my_set = set(collection)
# my_dict = dict(enumerate(collection))
# my_str = [str(i) for i in collection]
	
# result_list = list()
# tuple(map(result_list.append, my_list))
# tuple(map(result_list.append, my_tuple))
# tuple(map(result_list.append, my_set))
# tuple(map(result_list.append, my_dict))
# tuple(map(result_list.append, my_str))
	
# print(result_list)

# 4. Функция zip

# numbers = [2, 9, 18, 28]
# names = ["Дима", "Марина", "Андрей", "Никита"]

# for name, number in zip(names, numbers):
#     print(name, number)

# 5.Функция enumerate

# shopping_list = ("фрукты","овощи","чай","кофе","потанцуем")
# for index, item in enumerate(shopping_list):
#     print(f"index:{index}, раздел:{item}")

# 6.  list comprehension

# import random
# a = [random.randint(-10, 10) for i in range(10)]
# print(a)
# b = [elements for elements in a if elements < 0 and elements % 2 == 0]
# print(b)
# [-6, 6, -4, -4, -6, 10, -5, -1, -10, -7]
# [-6, -4, -4, -6, -10]